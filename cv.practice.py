import cv2 as cv
import matplotlib
from matplotlib.colors import is_color_like
from cv2 import cvtColor

cap=cv.VideoCapture(0)
width=int(cap.get(3))
hight=int(cap.get(4))
out=cv.VideoWriter('camera.mp4',cv.VideoWriter_fourcc('M','J','P','G'),30,(width,hight),isColor=False)
while cap.isOpened():
    ret,frame=cap.read()
    gray_frame=cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary_camera)=cv.threshold(gray_frame,127,255,cv.THRESH_BINARY)
    out.write(gray_frame)
    cv.imshow('camera',binary_camera)
    if cv.waitKey(1)& 0xff==ord('q'):
        break

cap.release()
cv.destroyAllWindows()
