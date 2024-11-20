import cv2 as cv


vdo=cv.VideoCapture(0)
vdo.set(10,0)#britness
vdo.set(3,1000)#width
vdo.set(4,1000)#hight

while vdo.isOpened():
    ret,frame=vdo.read()
    cv.imshow('camera',frame)
    if cv.waitKey(1)& 0xff==ord('q'):
        break

vdo.release()
cv.destroyAllWindows()
