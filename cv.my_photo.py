import cv2 as cv
import numpy as np
from cv2 import cvtColor
image=np.zeros((400,400))



image=np.zeros((400,400,3),np.uint8)
cv.imshow("black image",image)

image[:]=[147,20,255]
# cv.imshow("pink image",image)

# gray_image=cvtColor(image,cv.COLOR_BGR2GRAY)
# cv.imshow("gray image",gray_image)

image[200:300,200:300]=[0,255,0]

image_2=np.zeros((500,500))

image2=np.zeros((500,500,3),np.uint8)

cv.line(image_2,(5,5),(250,250),(255,255,255),2)
# image_2=cv.rectangle(image_2,(250,300),(400,500),(255,255,255),3)

#in other caree we also fill rectangle
cv.rectangle(image_2,(250,300),(400,500),(255,255,255),3)
cv.putText(image_2,'asim',(200,100),cv.FONT_HERSHEY_DUPLEX,2,(255,255,255),3)
cv.circle(image2,(100,250),50,(255,255,255),3)
cv.imshow("image",image_2)

# cv.imshow("shap image",image)

cv.waitKey(0)
cv.destroyAllWindows()

