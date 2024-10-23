import cv2
import numpy as np

img = cv2.imread('oranges.jpg')
cv2.imshow('img',img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

color = 20

color1 = [color-10,110,110]
color2 = [color+10,255,255]

color1 = np.array(color1,dtype=np.uint8)
color2 = np.array(color2,dtype=np.uint8)

mask = cv2.inRange(img,color1,color2)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
for contour in contours:
    if cv2.contourArea(contour) > 100:
        cv2.polylines(img,[contour],True,(255,255,255),2)

cv2.imshow('img',img)
cv2.waitKey(0)

