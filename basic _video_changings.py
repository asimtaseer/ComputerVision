import cv2 as cv
import numpy as np
from cv2 import cvtColor


cap=cv.VideoCapture(0)

# i use small resolution 
def small_resolution():
          cap.set(3,320)
          cap.set(4,240)

small_resolution()



while cap.isOpened():
     ret,frame=cap.read()
     gray_frame=cvtColor(frame,cv.COLOR_BGR2GRAY)
     gray_frame=cvtColor(gray_frame,cv.COLOR_GRAY2BGR)
     (thresh,binary_frame)=cv.threshold(gray_frame,127,255,cv.THRESH_BINARY)

     blur_frame=cv.GaussianBlur(gray_frame,(7,7),0)
 
     edge_frame=cv.Canny(gray_frame,7,7)
     edge_frame=cvtColor(edge_frame,cv.COLOR_GRAY2BGR)
     thickness_frame=cv.dilate(edge_frame,(3,3),iterations=1)
   
     erode_frame=cv.erode(thickness_frame,(3,3),iterations=1)
   
     stack1=np.hstack((frame,gray_frame,binary_frame))
   
     stack2=np.hstack((blur_frame,edge_frame,thickness_frame))
    
     stack3=np.vstack((stack1,stack2))
     cv.imshow('All',stack3)
     if cv.waitKey(1)&0xff==ord('q'):
             break


cap.release()
cv.destroyAllWindows()