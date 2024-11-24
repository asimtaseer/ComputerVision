import cv2 as cv
import numpy as np
from cv2 import cvtColor
#reading image 
image=cv.imread('resources/leaf.jpg')

# show image
cv.imshow('image',image)

gray_image=cvtColor(image,cv.COLOR_BGR2GRAY)
gray_image=cvtColor(gray_image,cv.COLOR_GRAY2BGR)
# cv.imshow('gray image',gray_image)
blur_image=cv.GaussianBlur(gray_image,(7,7),0)
# cv.imshow('biur image',blur_image)

(thresh,binary_image)=cv.threshold(gray_image,127,255,cv.THRESH_BINARY)
# cv.imshow('binary image',binary_image)

edge_image=cv.Canny(image,7,7)
edge_image=cvtColor(edge_image,cv.COLOR_GRAY2BGR)
# cv.imshow('edge image',edge_image)

# karnel=np.ones((3,3),np.uint8)

image_thickness=cv.dilate(edge_image,(3,3),iterations=1)
# cv.imshow('dilatred image',image_thickness)
image_erosion=cv.erode(image_thickness,(3,3),iterations=1)
# cv.imshow('erosion',image_erosion)


h_stack=np.hstack((image,gray_image,binary_image))
h_stack_2=np.hstack((edge_image,image_thickness,image_erosion))

all=np.vstack((h_stack,h_stack_2))

cv.imshow('all images',all)
cv.waitKey(0)
cv.destroyAllWindows()