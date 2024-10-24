import cv2
import numpy as np
img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5),np.uint8)
ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) 
erosion = cv2.erode(thresh,kernel)
dilation = cv2.dilate(thresh,kernel)

cv2.imshow('thresh',thresh)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)

cv2.waitKey(0)

