import cv2
import numpy as np
cap = cv2.VideoCapture('Апельсины.mp4')

while True:
    ret, frame = cap.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    color = 20
    color1 = [color-10,200,120]
    color2 = [color+10,255,255]
    color1 = np.array(color1,dtype=np.uint8)
    color2 = np.array(color2,dtype=np.uint8)
    mask = cv2.inRange(img,color1,color2)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            cv2.polylines(frame,[contour],True,(255,55,0),2)
    cv2.imshow('video orange', frame)
    if cv2.waitKey(33) == 27:
        break
cap.release()
cv2.destroyAllWindows()

