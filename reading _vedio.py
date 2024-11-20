import cv2 as cv

video=cv.VideoCapture('resources/WhatsApp Video 2024-11-14 at 12.30.44 AM.mp4')

while (video.isOpened()):
    ret,frame=video.read()
    if ret==True:
        cv.imshow('vediod',frame)
        if cv.waitKey(1)&0XFF==ord('q'):
            break
    else:
        break

video.release()
cv.destroyAllWindows()