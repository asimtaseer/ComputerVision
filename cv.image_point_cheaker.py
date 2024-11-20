import cv2 as cv
import numpy as np
import time

def pointer_cheaker(event,x,y,flag,parameters):
    global values
    if event==cv.EVENT_LBUTTONDOWN:
        value = list((x,y))
        values.append(value)
        font=cv.FONT_HERSHEY_PLAIN
        cv.putText(image,str(x)+','+str(y),(x,y),font,1,(0,255,255),thickness=1)
        if len(values)==4:
            im = crop_image(image, values)
            print(values)
            cv.imshow('image',im)
            time.sleep(10)
            exit()
        else:
            print(values)
        cv.imshow('image',image)
        
image=cv.imread('resources/images.jpg',1)
image=cv.resize(image,(400,500))

cv.imshow("image",image)
# print(image.shape)
cv.setMouseCallback('image',pointer_cheaker)
width=400
hight=500
values = []

def crop_image(image, values):
    point1=np.float32([values[0],values[1],values[2],values[3]])
    point_2=np.float32([[0,0],[width,0],[0,hight],[width,hight]])
    matrix=cv.getPerspectiveTransform(point1,point_2)
    out_image=cv.warpPerspective(image,matrix,(width,hight))
    cv.imshow('new image',out_image)
    cv.imwrite('images_.png', out_image)
    print("Image croped and saved successfully")
    return out_image

point1=np.float32([[163,71],[341,112],[29,284],[245,366]])
point_2=np.float32([[0,0],[width,0],[0,hight],[width,hight]])
matrix=cv.getPerspectiveTransform(point1,point_2)
out_image=cv.warpPerspective(image,matrix,(width,hight))
cv.imshow('new image',out_image)



cv.waitKey(0)
cv.destroyAllWindows()
