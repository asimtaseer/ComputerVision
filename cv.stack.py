import numpy as np
import cv2 as cv
from cv2 import cvtColor
image=cv.imread('resources/images.jpg')

# cv.imshow('image',image)
h_stack=np.hstack((image,image))
gray_image=cvtColor(image,cv.COLOR_BGR2GRAY)
blured=cv.GaussianBlur(gray_image,(7,7),0)
# cv.imshow('stack image',h_stack)
cv.imshow('gray image',gray_image)
blured=cvtColor(blured,cv.COLOR_GRAY2BGR)


# vertical stack

# cv.imshow('blur image',blured)
v_stack=np.vstack((image,blured))
cv.imshow('vertical stack',v_stack)


cv.waitKey(0)
cv.destroyAllWindows()
