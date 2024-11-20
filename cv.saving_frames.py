import cv2 as cv
import numpy as np

cap=cv.VideoCapture('resources/talha.mp4')
frame_number=0
while cap.isOpened():
    ret,frame=cap.read()
    cv.imwrite(f"resources/frames/frame_{frame_number}.jpg",frame)
    frame_number=frame_number+1



cap.release()
cv.destroyAllWindows
