import cv2 as cv


img=cv.imread('resources/images.jpg')
#cv.imshow('image',img)
img2=cv.resize(img,(400,400))
#cv.imshow('image2',img2)
from cv2 import cvtColor
 
gray_image=cvtColor(img2,cv.COLOR_BGR2GRAY)
#cv.imshow('gray image',gray_image)
(thresh,binary_image)=cv.threshold(gray_image,127,255,cv.THRESH_BINARY)
#cv.imshow('binary image',binary_image)

vedio=cv.VideoCapture('resources/WhatsApp Video 2024-11-14 at 12.30.44 AM.mp4')

while (vedio.isOpened()):
    ret,frame=vedio.read()
    cv.imshow('frame',frame)
    if cv.waitKey(1)& 0XFF==ord('q'):
            break
    

#cv.waitKey(0)
vedio.release()
cv.destroyAllWindows()
