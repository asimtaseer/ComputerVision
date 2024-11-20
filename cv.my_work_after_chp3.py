import cv2 as cv

Img= cv.imread('resources/Nikon-D750-sample-photo1.jpg')

cv.imshow('first image ',Img)

image2= cv.imread('resources/WhatsApp Image 2024-11-12 at 11.45.02 PM.jpeg')
image2=cv.resize(image2,(600,400))

cv.imshow('image2',image2)


from cv2 import cvtColor

gray_image=cvtColor(image2,cv.COLOR_BGR2GRAY)

cv.imshow('Gray image',gray_image)

cv.waitKey(0)
cv.destroyAllWindows()
