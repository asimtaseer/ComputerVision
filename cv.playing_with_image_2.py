# original image
# resize
# gray
# black and white
# blur
# edge detection
# thickness
# erosion 
# crop

import cv2 as cv
from cv2 import cvtColor
image=cv.imread("resources/WhatsApp Image 2024-11-12 at 11.45.02 PM.jpeg")
# cv.imshow("image",image)

resize_image=cv.resize(image,(400,500))
cv.imshow("resize image",resize_image)

# gray_image=cvtColor(resize_image,cv.COLOR_BGR2GRAY)
# cv.imshow("gray image",gray_image)

# (thresh,binary_image)=cv.threshold(gray_image,127,255,cv.THRESH_BINARY)
# cv.imshow("binary image",binary_image)

# blur_image=cv.GaussianBlur(resize_image,(7,7),1)
# cv.imshow("blur image",blur_image)

# edge_detection=cv.Canny(resize_image,47,47)
# cv.imshow("edge image",edge_detection)

# # thick_image=cv.dilate(edge_detection,(7,7),iterations=1)
# # cv.imshow("thick image",thick_image)

# import numpy as np

# mat_karnel=np.ones((3,3),np.uint8)
# thick_2=cv.dilate(edge_detection,mat_karnel,iterations=1)
# cv.imshow("thick",thick_2)

# erod_image=cv.erode(thick_2,mat_karnel,iterations=1)
# cv.imshow("erod image",erod_image)

print("The size of image is ",resize_image.shape)

crop_image=resize_image[50:300,50:300]

cv.imshow('crop image',crop_image)

cv.waitKey(0)
cv.destroyAllWindows()