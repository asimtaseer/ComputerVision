import cv2 as cv
import numpy as np

image=np.ones((400,400))
image_2=np.zeros((400,400))

image_2=np.zeros((400,400,3),np.uint8)

image_2[:]=0,0,255#red
image_2[50:150,50:250]=0,255,255#shape in yellow

cv.line(image_2,(9,9),(200,200),(255,0,0),3)#line in blue
cv.circle(image_2,(270,130),60,(255,255,255),2)
image_2=cv.rectangle(image_2,(220,230),(350,300),(0,255,255),3)
# cv.imshow('white',image)
cv.putText(image_2,"ASIM",(200,350),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)
cv.imshow("black",image_2)

cv.waitKey(0)
cv.destroyAllWindows()
