import cv2 as cv

video=cv.VideoCapture(0)

while video.isOpened():
    ret,frame=video.read()
    if ret==True:
        cv.imshow("camera",frame)
        if cv.waitKey(1)& 0xff==ord('q'):
            break
    else:
        break

video.release()
cv.destroyAllWindows()