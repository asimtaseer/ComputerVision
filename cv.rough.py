import cv2 as cv
import numpy as np
from cv2 import cvtColor

# image=cv.imread('resources/leaf.jpg')
# width=image.shape[1]

# hight=image.shape[0]

# image2=cv.imread('resources/images.jpg')
# print(image.shape)
# print(width)
# print(hight)
# # image=cv.resize(image,(400,400))
# cv.imshow('image',image)

# def same_converter(x):
    
#     x=cv.resize(x,(width,hight))

# same_converter(image2)
# image2=cv.resize(image2,(width,hight))
# cv.imshow('image2',image2)
# cv.waitKey(0)



cap=cv.VideoCapture(0)
cap.set(3,320)
cap.set(4,220)

width=cap.get(3)
hight=cap.get(4)
while cap.isOpened():
    ret,frame=cap.read()
    blur_frame=cv.GaussianBlur(frame,(7,7),0)

    # cv.imshow('video',frame)
    stack1=np.hstack((frame,blur_frame))
    cv.imshow('video',stack1)
    if cv.waitKey(1)&0xff==ord('q'):
        break

cv.destroyAllWindows()