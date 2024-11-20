import cv2 as cv
import numpy as np

def pointer_cheaker(event, x, y, flags, parameters):
    global values
    if event == cv.EVENT_LBUTTONDOWN:
        
        value = [x, y]
        values.append(value)

        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(image, f"{x-5},{y-20}", (x, y-20), font, 1, (0, 255, 255), thickness=1)

        if len(values) == 4:
            crop_image(image, values)
            print(f"Selected points: {values}")
            cv.waitKey(0)
        else:
            print(f"Current points: {values}")
        
        cv.imshow('image', image)

def crop_image(image, values):
    width, height = 400, 500 

    point1 = np.float32([values[0], values[1], values[2], values[3]])
    
    point_2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    matrix = cv.getPerspectiveTransform(point1, point_2)

    out_image = cv.warpPerspective(image, matrix, (width, height))
    cv.destroyWindow('image')
    cv.imshow('Cropped Image', out_image)

    cv.imwrite('images_cropped.png', out_image)
    print("Image cropped and saved successfully.")

image = cv.imread('resources/document.jpg', 1)

if image is None:
    print("Error: Image not found!")
else:
    image = cv.resize(image, (600, 800)) 

    values = [] 

    # Display the original image
    cv.imshow("Original Image", image)
    print(f"Image dimensions: {image.shape}")

    # Set the mouse callback to capture the points
    cv.setMouseCallback('Original Image', pointer_cheaker)

    # Wait for user interaction
    cv.waitKey(0)
    cv.destroyAllWindows()
