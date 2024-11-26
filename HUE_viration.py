import cv2 as cv 
from cv2 import cvtColor
import numpy as np

path='resources/leaf.jpg'

# img= cv.imread(path)
# cv.imshow('image',img)
def slider():
    print("In function")


cv.namedWindow('HSV')
cv.resizeWindow('HSV',(500,400))

cv.createTrackbar('Hue_min','HSV',0,179,slider)
cv.createTrackbar('Hue_max','HSV',179,179,slider)
cv.createTrackbar('Sat_min','HSV',0,255,slider)
cv.createTrackbar('Sat_max','HSV',255,255,slider)
cv.createTrackbar('Val_max','HSV',0,255,slider)
cv.createTrackbar('Val_min','HSV',255,255,slider)


while True:
    image=cv.imread(path)
    hsv_image=cvtColor(image,cv.COLOR_BGR2HSV)
    hue_min=cv.getTrackbarPos('Hue_min','HSV')
    hue_max=cv.getTrackbarPos('Hue_max','HSV')
    sat_min=cv.getTrackbarPos('Sat_min','HSV')
    sat_max=cv.getTrackbarPos('Sat_max','HSV')
    val_min=cv.getTrackbarPos('Val_min','HSV')
    val_max=cv.getTrackbarPos('Val_max','HSV')
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)

    lower=np.array([hue_min,sat_min,val_min])
    upper=np.array([hue_max,sat_max,val_max])
    mask_image=cv.inRange(hsv_image,lower,upper)
    out_image=cv.bitwise_and(image,image,mask=mask_image)

    cv.imshow('image',image)
    # cv.imshow('hsv_image',hsv_image)
    cv.imshow('mask image',mask_image)
    cv.imshow('final image',out_image)
    if cv.waitKey(1)&0xff==ord('q'):
        break
    

cv.destroyAllWindows()