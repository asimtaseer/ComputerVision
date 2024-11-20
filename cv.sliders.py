import cv2 as cv
import numpy as np
from cv2 import cvtColor
path='resources/leaf.jpg'
image=cv.imread('resources/leaf.jpg')
def slider():
    pass
# cv.imshow('leaf',image)
hsv_image=cvtColor(image,cv.COLOR_BGR2HSV)
# cv.imshow("HSV",hsv_image)
cv.namedWindow('sliders')
hue_min=cv.createTrackbar('hue min','sliders',0,179,slider)
hue_max=cv.createTrackbar('hue max','sliders',179,179,slider)
sat_min=cv.createTrackbar('seturation min','sliders',0,255,slider)
sat_max=cv.createTrackbar('seturation max','sliders',255,255,slider)
val_min=cv.createTrackbar('value min','sliders',0,255,slider)
val_max=cv.createTrackbar('value max','sliders',255,255,slider)

while True:
    image=cv.imread('resources/leaf.jpg')
    hsv_image=cvtColor(image,cv.COLOR_BGR2HSV)
    hue_min=cv.getTrackbarPos('hue min','sliders')
    hue_max=cv.getTrackbarPos('hue max','sliders')
    sat_min=cv.getTrackbarPos('seturation min','sliders')
    sat_max=cv.getTrackbarPos('seturation max','sliders')
    val_min=cv.getTrackbarPos('value min','sliders')
    val_max=cv.getTrackbarPos('value max','sliders')
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)
    lower=np.array([hue_min,sat_min,val_min])
    upper=np.array([hue_max,sat_max,val_max])
    mask_image=cv.inRange(hsv_image,lower,upper)
    out_image=cv.bitwise_and(image,image,mask=mask_image)
    cv.imshow('mask',mask_image)
    cv.imshow('final image',out_image)
    if cv.waitKey(0)&0xff==ord('q'):
        break
cv.destroyAllWindows()