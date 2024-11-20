import cv2 as cv

img=cv.imread('resources/Nikon-D750-sample-photo1.jpg')
cv.imshow('firstimage',img)

img2= cv.resize(img,(600,400))
cv.imshow('second image',img2)
cv.waitKey(0)
cv.destroyAllWindows()
