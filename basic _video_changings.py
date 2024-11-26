import cv2 as cv
import numpy as np
from cv2 import cvtColor

# reding camera

cap=cv.VideoCapture(0)

# convert into small resolution 
def small_resolution():
          cap.set(3,320)
          cap.set(4,240)

# functio is called to small the resolution
small_resolution()

# reading the camera

while cap.isOpened():
#      returning frames below
     ret,frame=cap.read()
#      gray frames
     gray_frame=cvtColor(frame,cv.COLOR_BGR2GRAY)


#        convert back to BGR because i stack all camera at the end
        # below i also display gray cam so i use all BGR videos
     gray_frame=cvtColor(gray_frame,cv.COLOR_GRAY2BGR)


#      converted into binary
     (thresh,binary_frame)=cv.threshold(gray_frame,127,255,cv.THRESH_BINARY)


#      convert video into blur video
     blur_frame=cv.GaussianBlur(gray_frame,(7,7),0)


#        shows the edges of video
     edge_frame=cv.Canny(gray_frame,7,7)


#      convert back to BGR because i stack all camera at the end in BGR platform
     edge_frame=cvtColor(edge_frame,cv.COLOR_GRAY2BGR)


#      thickness of video
     thickness_frame=cv.dilate(edge_frame,(3,3),iterations=1)


#    erode video
     erode_frame=cv.erode(thickness_frame,(3,3),iterations=1)


#    stacking three cameras using numpy
     stack1=np.hstack((frame,gray_frame,binary_frame))


#    staking other three cameras using numpy
     stack2=np.hstack((blur_frame,edge_frame,thickness_frame))

     
#      main stack to display all cameras
#        virtical stack
     stack3=np.vstack((stack1,stack2))


#      show all the cameras
     cv.imshow('All',stack3)

#      condition is used to close the cameras
     if cv.waitKey(1)&0xff==ord('q'):
             break


cap.release()
cv.destroyAllWindows()