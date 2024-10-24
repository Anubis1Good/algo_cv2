import cv2
import numpy as np
img = cv2.imread('Bin.jpg')
img = cv2.resize(img,(img.shape[1]//4,img.shape[0]//4))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5),np.uint8)
ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) 
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow('thresh',thresh)
cv2.imshow('opening',opening)
cv2.imshow('closing',closing)

cv2.waitKey(0)

