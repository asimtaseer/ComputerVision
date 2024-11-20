import cv2 as cv
from cv2 import cvtColor
import numpy as np
image=cv.imread('resources/images.jpg')
#cv.imshow('original image',image)

# gray_image=cvtColor(image,cv.COLOR_BGR2GRAY)
# cv.imshow('gray image',gray_image)

# (thresh,binary)=cv.threshold(gray_image,127,255,cv.THRESH_BINARY)
# cv.imshow("binary image",binary)

# blur_image=cv.GaussianBlur(image,(7,7),0,)
# cv.imshow('blur image',blur_image)

# resize_image= cv.resize(image,(400,400))
# cv.imshow('resized image',resize_image)

# edge_image=cv.Canny(image,45,45)
# cv.imshow('edge detection',edge_image)

# mat_karnel=np.ones((3,3),np.uint8)
# thick_image=cv.dilate(edge_image,(mat_karnel),iterations=1)
# cv.imshow('dilated image',thick_image)

# ero_image=cv.erode(thick_image,mat_karnel,iterations=1)
# cv.imshow('erosion',ero_image)

# (thresh,black_and_white_image)=cv.threshold(image,100,255,cv.THRESH_BINARY)
# cv.imshow('black and white',black_and_white_image)
# # thck_image=cv.dilate(edge_image,(7,7),iterations=1)
# cv.imshow('dilated image',thck_image)

image=cv.resize(image,(400,400))
cv.imshow('resize',image)
print("The size of image is ",image.shape)
crop_image=image[150:350,150:350]
cv.imshow("crop image",crop_image)
cv.waitKey(0)
cv.destroyAllWindows()