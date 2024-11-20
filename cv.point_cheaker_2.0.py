import cv2 as cv
import numpy as np


def point_cheaker(event,x,y,flag,parameters):
        if event==cv.EVENT_LBUTTONDOWN:
             print(x,'',y)
             font=cv.FONT_HERSHEY_PLAIN
            #  cv.putText(image,str(x)+','+str(y),(x,y),font,1,(0,255,255),thickness=1)
             cv.circle(image,(x,y),10,(0,255,0),thickness=1)
             cv.imshow('image',image)
     
        if event==cv.EVENT_RBUTTONDOWN:
               print(x,'',y)
               font_2=cv.FONT_HERSHEY_PLAIN
               b=image[x,y,0]
               g=image[x,y,1]
               r=image[x,y,2]
               cv.putText(image,str(b)+','+str(g)+','+str(r),(x,y),font_2,1,(0,255,255),thickness=1)
               cv.imshow('image',image)


image=cv.imread('resources/images.jpg',1)
image=cv.resize(image,(500,500))
cv.imshow('image',image)
cv.setMouseCallback('image',point_cheaker)
cv.waitKey(0)
cv.destroyAllWindows()

