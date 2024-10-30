import cv2
import numpy as np
import mediapipe as mp

# Подключаем камеру
cap = cv2.VideoCapture(0) 

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False)
npDraw = mp.solutions.drawing_utils

while True: 
    ret, img = cap.read()
    img = cv2.flip(img,1) # отзеркалить камеру

    results = hands.process(img)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            for id, lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                if  id == 8 or id == 12:
                    cv2.circle(img, (cx,cy),10,(255,0,255),cv2.FILLED)

            npDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cv2.imshow('hands', img)
    if cv2.waitKey(20) == 27: # exit on ESC
        break
        
cap.release()
cv2.destroyAllWindows()


