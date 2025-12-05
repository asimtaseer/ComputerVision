import cv2
# use the app (ip camera)
url='enter you ip camera url here'

cap=cv2.VideoCapture(url)

while True:
    ret , frame= cap.read()
    if frame is not None:
        frame=cv2.resize(frame,(500,300))
        cv2.imshow('camera',frame)
        
