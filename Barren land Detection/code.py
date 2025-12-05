import cv2
import numpy as np
import os
import csv
from datetime import datetime

def get_berlin_roi(image):
    """Define a central region as 'Berlin Land'."""
    h, w = image.shape[:2]
    roi_x, roi_y = int(w * 0.4), int(h * 0.4)
    roi_w, roi_h = int(w * 0.2), int(h * 0.2)
    return roi_x, roi_y, roi_w, roi_h


def analyze_frame(frame):
    """Analyze a single video frame."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color masks
    vegetation_mask = cv2.inRange(hsv, (25, 40, 20), (85, 255, 255))   # Green
    water_mask      = cv2.inRange(hsv, (90, 50, 20), (140, 255, 255))  # Blue
    barren_mask     = cv2.inRange(hsv, (5, 20, 50), (35, 255, 200))    # Brown
    sky_mask        = cv2.inRange(hsv, (85, 0, 120), (130, 255, 255))  # Sky

    total_pixels = frame.shape[0] * frame.shape[1]
    vegetation = np.count_nonzero(vegetation_mask)
    water = np.count_nonzero(water_mask)
    barren = np.count_nonzero(barren_mask)
    sky = np.count_nonzero(sky_mask)

    effective_total = vegetation + water + barren
    effective_total = max(effective_total, 1)

    veg_ratio = (vegetation / effective_total) * 100
    water_ratio = (water / effective_total) * 100
    barren_ratio = (barren / effective_total) * 100
    sky_ratio = (sky / total_pixels) * 100

    #Analyze largest water body
    contours, _ = cv2.findContours(water_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_blob = max([cv2.contourArea(c) for c in contours], default=0)
    largest_blob_ratio = (largest_blob / total_pixels) * 100

    # Decision logic
    if water_ratio > 10 or largest_blob_ratio > 5:
        decision = "Do NOT drop seed (Water detected)"
        color = (0, 0, 255)
    elif barren_ratio > veg_ratio and barren_ratio > 20:
        decision = "DROP seed (Barren > Vegetation)"
        color = (0, 255, 0)
    elif veg_ratio > 20:
        decision = " Do NOT drop seed (Vegetation dominant)"
        color = (0, 0, 255)
    else:
        decision = "Uncertain area (Manual check recommended)"
        color = (0, 255, 255)

    #Copy original frame to draw overlays
    output_frame = frame.copy()

    # Draw ONLY top-level barren areas (no nested rectangles)
    barren_contours, hierarchy = cv2.findContours(
        barren_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
    )

    MIN_BARREN_AREA = 500000  # ignore small areas

    if hierarchy is not None:
        hierarchy = hierarchy[0]  # flatten structure
        for idx, cnt in enumerate(barren_contours):

            # Draw only top-level contours (no parents inside)
            if hierarchy[idx][3] != -1:  
                continue   # skip nested contours

            area = cv2.contourArea(cnt)
            if area > MIN_BARREN_AREA:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(output_frame, (x, y), (x + w, y + h), (0, 165, 255), 2)
                cv2.putText(output_frame, f"Barren ({int(area)}px)", (x, y - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 165, 255), 1)

    # Display decision and stats
    cv2.putText(output_frame, decision, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    cv2.putText(output_frame,
                f"Veg: {veg_ratio:.1f}%  Wat: {water_ratio:.1f}%  Bar: {barren_ratio:.1f}%",
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    return output_frame, decision, veg_ratio, water_ratio, barren_ratio, sky_ratio, largest_blob_ratio


def log_analysis(veg, water, barren, sky, blob, decision):
    log_file = "land_analysis_log.csv"
    file_exists = os.path.isfile(log_file)
    with open(log_file, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Vegetation %", "Water %", "Barren %", "Sky %", "Largest Water Blob %", "Decision"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            f"{veg:.2f}",
            f"{water:.2f}",
            f"{barren:.2f}",
            f"{sky:.2f}",
            f"{blob:.2f}",
            decision
        ])


def main():
    cap = cv2.VideoCapture('resources/VID_20251127_151213.mp4')  # or 0 for live camera
    if not cap.isOpened():
        print(" Camera or video not found.")
        return

    print("🎥 Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video or cannot read frame.")
            break

        analyzed_frame, decision, veg, water, barren, sky, blob = analyze_frame(frame)
        cv2.imshow(" Land Analysis (Press 'q' to quit)", analyzed_frame)

        log_analysis(veg, water, barren, sky, blob, decision)

        if cv2.waitKey(40) & 0xFF == ord('q'):
            print("\n Exiting on user command.")
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
