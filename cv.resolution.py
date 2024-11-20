import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

def hd_resolution():
        cap.set(3,400)
        cap.set(4,600)
hd_resolution()
width=int(cap.get(3))
hight=int(cap.get(4))

out=cv.VideoWriter('my camera.mp4',cv.VideoWriter_fourcc('M','J','P','G'),30,(width,hight))
while cap.isOpened():
        ret,frame=cap.read()
        out.write(frame)
        cv.imshow('camera',frame)
        if cv.waitKey(1)& 0xff==ord('q'):
                break
        
cap.release()
cv.destroyAllWindows()