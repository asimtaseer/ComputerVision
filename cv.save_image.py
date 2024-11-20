import cv2 as cv
from cv2 import cvtColor
image=cv.imread('resources/Nikon-D750-sample-photo1.jpg')
gray_image=cvtColor(image,cv.COLOR_BGR2GRAY)

(thresh,black_and_whiite_image)=cv.threshold(gray_image,127,255,cv.THRESH_BINARY)
black_and_whiite_image=cv.resize(black_and_whiite_image,(400,500))
cv.imwrite('resources/black_and_white.png',black_and_whiite_image)
