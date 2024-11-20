import cv2 as cv

cap=cv.VideoCapture('resources/WhatsApp Video 2024-11-14 at 12.30.44 AM.mp4')

if(cap.isOpened()==False):
 print("Error")


ret, frame = cap.read()

while ret:
  cv.imshow("read", frame)
  ret, frame = cap.read()

  keycode = cv.waitKey(1)
  if keycode != -1:
    break

cap.release()
cv.destroyAllWindows()