import cv2 as cv
from cv2 import cvtColor

img=cv.imread('resources/Nikon-D750-sample-photo1.jpg')

gray_img =cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('gray image',gray_img)  

cv.waitKey(0)
cv.destroyAllWindows()
