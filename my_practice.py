import cv2 as cv
from cv2 import cvtColor
img=cv.imread('resources/images.jpg')
#cv.imshow('image',img)

gray_image=cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray image',gray_imagee)
(thresh,binary_image)=cv.threshold(gray_image,127,255,cv.THRESH_BINARY)
#cv.imshow('binary image',binary_image)
binary_image=cv.resize(binary_image,(400,500))
#cv.imshow('binary image',binary_image)
#cv.imwrite('black and white.jpg',binary_image)
cv.waitKey(0)
cv.destroyAllWindows()

#vedio

my_v=cv.VideoCapture('resources/blue.mp4')

# while my_v.isOpened():
#     ret,frame=my_v.read()
#     if ret==True:
#         cv.imshow('vedio',frame)
#         if cv.waitKey(1)& 0xff==ord('q'):
#             break
#     else:
#         break

# my_v.release()
# cv.destroyAllWindows()

#now gray vedio 
 
# while my_v.isOpened():
#     ret,frame=my_v.read()
#     grayframe= cvtColor(frame,cv.COLOR_BGR2GRAY)
#     (thresh,binary_vedio)=cv.threshold(frame,127,255,cv.THRESH_BINARY)
#     if ret==True:
#         #cv.imshow('gray vedio',grayframe)
#         cv.imshow('binary vedio',binary_vedio)
#         if cv.waitKey(1)& 0xff==ord('q'):
#              break
#     else:
#         break

# my_v.release()
# cv.destroyAllWindows()


#vedio save:
from matplotlib.colors import is_color_like
w=int(my_v.get(3))
h=int(my_v.get(4))

out=cv.VideoWriter('bluevedio.avi',cv.VideoWriter_fourcc('M','J','P','G'),10,(w,h),isColor=False)

while True:
    ret,frame=my_v.read()
    if ret==True:
        out.write(frame) 
        cv.imshow('vedio',frame)
        if cv.waitKey(1)& 0xff==ord('q'):
            break
    else:
        break

my_v.release()
out.release()
cv.destroyAllWindows()
