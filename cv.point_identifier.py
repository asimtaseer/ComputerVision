import cv2 as cv
import numpy as np


def point_cheaker(event,x,y,flag,prameters):
        if event==cv.EVENT_FLAG_LBUTTON:
          print(x,'',y)
          font=cv.FONT_HERSHEY_PLAIN
          cv.putText(imag,str(x)+','+str(y),(x,y),font,1,(0,0,255),thickness=1)
          cv.imshow('image',imag)


if __name__=="__main__":
      imag=cv.imread('resources/document.jpg',1)
      cv.imshow('image',imag)
      cv.setMouseCallback('image',point_cheaker)
      cv.waitKey(0)
      cv.destroyAllWindows

