import cv2 as cv
from cv2 import cvtColor

# image=cv.imread('resources/images.jpg')
# cv.imshow("image",image)

# gray_image=cvtColor(image,cv.COLOR_BGR2GRAY)

# cv.imshow('gray image',gray_image)

import numpy as np
width=int(input("Enter width of image"))
hight=int(input("Enter hight of image"))
color=input("Enter the background color: ")
if color=='Red'or color=='red':
      my_image=np.ones((width,hight))
      my_image=np.ones((width,hight,3),np.uint8)
      my_image[:]=0,0,255

shape=input("Enter the shape you want to draw")

if shape=='circle' or shape=='Circle':
      center_point_x=int(input("Enter x axis center point"))
      center_point_y=int(input("Enter y axis center point"))
      r=int(input("Enter Radius"))
      color_circle=input("Enter the color: ")
      if color_circle=='white'or color_circle=='White':
           c_color=[255,255,255]

      thickness=int(input("Enter thickness of circle"))
      my_image=cv.circle(my_image,(center_point_x,center_point_y),r,255,255,255,thickness)

cv.imshow('image ',my_image)

cv.waitKey(0)
cv.destroyAllWindows()