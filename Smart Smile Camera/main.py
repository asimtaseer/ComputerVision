import cv2
import os

video = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
smileCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

# SAVE FOLDER
save_dir = r"D:\CS&IT\python codes\capture"
os.makedirs(save_dir, exist_ok=True)

cnt = 500  

while True:
    success, img = video.read()
    if not success:
        print("Camera read failed")
        break

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayImg, 1.1, 4)

    keyPressed = cv2.waitKey(1)

    for (x,y,w,h) in faces:
        # cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0), 3)

        smiles = smileCascade.detectMultiScale(grayImg, 1.8, 15)

        for (sx,sy,sw,sh) in smiles:
            # cv2.rectangle(img, (sx,sy), (sx+sw,sy+sh), (100,100,100), 5)

            filename = f"image_{cnt}.jpg"
            path = os.path.join(save_dir, filename)

            saved = cv2.imwrite(path, img)

            if saved:
                print("Image saved at:", path)
                cnt += 1
            else:
                print("Image NOT saved")

            if cnt >= 503:
                break

    cv2.imshow('live video', img)

    if keyPressed & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
