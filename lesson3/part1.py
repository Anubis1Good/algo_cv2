import cv2
import numpy as np
img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 80, 0.01, 10) 
corners = np.int0(corners) 
  
for i in corners: 
    x, y = i.ravel() 
    cv2.circle(img, (x, y), 3, (250,55,200), -1) 


cv2.imshow('img',img)
cv2.waitKey(0)

