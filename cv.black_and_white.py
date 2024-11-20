import cv2 as cv
from cv2 import cvtColor
img=cv.imread('resources/Nikon-D750-sample-photo1.jpg')
cv.imshow('image',img)
gray_image= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

(thresh,binary_image)=cv.threshold(gray_image,127,255,cv.THRESH_BINARY)
cv.imshow('binary image',binary_image)
cv.waitKey(0)
cv.destroyAllWindows()