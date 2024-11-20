import cv2 as cv
import numpy as np
from cv2 import cvtColor


cap=cv.VideoCapture(0)


def small_resolution():
          cap.set(3,320)
          cap.set(4,240)

small_resolution()



while cap.isOpened():
     ret,frame=cap.read()
     gray_frame=cvtColor(frame,cv.COLOR_BGR2GRAY)
     gray_frame=cvtColor(gray_frame,cv.COLOR_GRAY2BGR)
     (thresh,binary_frame)=cv.threshold(gray_frame,127,255,cv.THRESH_BINARY)
    #  binary_frame=cvtColor(binary_frame,cv.COLOR_GRAY2BGR)
     blur_frame=cv.GaussianBlur(gray_frame,(7,7),0)
    #  blur_frame=cvtColor(blur_frame,cv.COLOR_GRAY2BGR)
     edge_frame=cv.Canny(gray_frame,7,7)
     edge_frame=cvtColor(edge_frame,cv.COLOR_GRAY2BGR)
     thickness_frame=cv.dilate(edge_frame,(3,3),iterations=1)
    #  thickness_frame=cvtColor(thickness_frame,cv.COLOR_GRAY2BGR)
     erode_frame=cv.erode(thickness_frame,(3,3),iterations=1)
    #  erode_frame=cvtColor(erode_frame,cv.COLOR_GRAY2BGR)
    #  cv.imshow("video",frame)
    #  cv.imshow('gray video',gray_frame)
    #  cv.imshow('binary video',binary_frame)
    #  cv.imshow('blur video',blur_frame)
    #  cv.imshow('edge video',edge_frame)
    #  cv.imshow('dilated video',thickness_frame)
    #  cv.imshow('erode video',erode_frame)
   #  stack1=np.hstack((frame,gray_frame,binary_frame))
    #  stack2=np.hstack((blur_frame,edge_frame,thickness_frame))
    #  stack3=np.vstack((stack1,stack2))
    #  cv.imshow('all',stack3)

     stack1=np.hstack((frame,gray_frame,binary_frame))
    #  stack1=cvtColor(stack1,cv.COLOR_GRAY2BGR)
    #  cv.imshow('stack 1',stack1)
     stack2=np.hstack((blur_frame,edge_frame,thickness_frame))
    #  stack2=cvtColor(stack2,cv.COLOR_GRAY2BGR)
    #  cv.imshow('stack 2',stack2)
     stack3=np.vstack((stack1,stack2))
     cv.imshow('All',stack3)
     if cv.waitKey(1)&0xff==ord('q'):
             break


cap.release()
cv.destroyAllWindows()