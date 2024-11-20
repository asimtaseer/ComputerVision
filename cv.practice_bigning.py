import cv2 as cv 

img=cv.imread('resources/Nikon-D750-sample-photo1.jpg')


img=cv.resize(img,(400,300))


from cv2 import cvtColor
gray_image=cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('gray image',gray_image)

cv.waitKey(0)
cv.destroyAllWindows()

