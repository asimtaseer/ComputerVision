import cv2 as cv
from matplotlib.colors import is_color_like
video= cv.VideoCapture('resources/blue.mp4')

w=int(video.get(3))
h=int(video.get(4))

out= cv.VideoWriter('vedio.mp4',cv.VideoWriter_fourcc('M','J','P','G'),10,(w,h),isColor=False)

while True:
    ret,frame=video.read()
    if ret==True:
        out.write(frame)
        cv.imshow('vedio',frame)        
        if cv.waitKey(1)&0xff==ord('q'):
            break
    else:
        break
video.release()
out.release()
cv.destroyAllWindows()
