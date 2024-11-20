import cv2 as cv
from cv2 import cvtColor
vdo=cv.VideoCapture(0)

while vdo.isOpened():
    ret,frame=vdo.read()
    gray_came=cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary_came)=cv.threshold(gray_came,127,255,cv.THRESH_BINARY)
    cv.imshow('camera',frame)
    cv.imshow('gray camera',gray_came)
    cv.imshow('binary camera',binary_came)
    if cv.waitKey(1)&0xff==ord('q'):
        break

vdo.release()
cv.destroyAllWindows()
