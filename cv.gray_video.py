import  cv2 as cv

from cv2 import cvtColor

video=cv.VideoCapture('resources/blue.mp4')

while(video.isOpened()):
    ret,frame=video.read()
    #gray_vedio=cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary)=cv.threshold(frame,200,255,cv.THRESH_BINARY)
    if ret==True:
        cv.imshow('vedio',binary)
        if cv.waitKey(1)&0xff==ord('q'):
            break
    else:
        break

video.release()
cv.destroyAllWindows()
