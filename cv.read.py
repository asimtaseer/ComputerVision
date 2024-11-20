

import cv2 as cv

img=cv.imread('resources/Nikon-D750-sample-photo1.jpg')
cv.imwrite('resources/Nikon-D750-sample-photo1.jpg',img)
#cv.imshow('Image',img)

cv.waitKey(0)