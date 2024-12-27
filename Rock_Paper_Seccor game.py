
import cv2 as cv
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random

cap=cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

detector=HandDetector(maxHands=1)

timer=0
start_game=False
state_result=False
score=[0,0]



while cap.isOpened():
    image=cv.imread('resources/background.jpeg')
    AI_Pic=cv.imread('resources/ai image.jpeg')
    AI_Pic=cv.resize(AI_Pic,(217,300))
    image=cv.resize(image,(600,500))
    # cv.imwrite('resources/resized_frame.jpeg',image)
    ret,frame=cap.read()
    if ret==True:
        frame=cv.resize(frame,(217,300))
        
        (hands,img)=detector.findHands(frame)

        if start_game:

            if state_result ==False:
                timer=time.time()-initinal_time
                cv.putText(image,str(int(timer)),(290,252),cv.FONT_HERSHEY_COMPLEX,1,(0,165,255),2)
                if timer>3:
                    state_result=True
                    timer=0
            
                    if hands:
                    #    player_move=None
                       hands=hands[0]
                       fingers=detector.fingersUp(hands)
                       if fingers==[0,0,0,0,0]:
                           player_move=1
                       if fingers==[0,1,1,0,0]:
                           player_move=2
                       if fingers==[1,1,1,1,1]:
                           player_move=3
                          
                    print(player_move)
                    random_values=random.randint(1,3)
                    
                    AI_image=cv.imread(f'resources/{random_values}.png',cv.IMREAD_UNCHANGED)
                    
                    if player_move==1 and random_values==3 or player_move==2 and random_values==3 or player_move==3 and random_values==1:
                        score[0]+=1

                    if random_values==1 and player_move==2 or random_values==2 and player_move==3 or random_values==3 and player_move==1:
                        score[1]+=1
                
                
                       
        
        cv.putText(image,str(score[0]),(229,89),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv.putText(image,str(score[1]),(503,90),cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)

        image[101:401,55:272]=frame
        image[99:399,333:550]=AI_Pic

        if state_result:
            AI_image=cv.resize(AI_image,(217,300))
            image[99:399,333:550]=AI_image
        cv.imshow('image',image)
        # cv.imshow('camera',frame)
        key=cv.waitKey(1)

        if key==ord('s'):
            start_game=True
            initinal_time=time.time()
            state_result=False
            


        if key&0xff==ord('q'):
            break
    else:
          break

cap.release()
cv.destroyAllWindows()
