import cv2
import numpy as np
img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

median = cv2.medianBlur(img, 5) 
cv2.imshow('Median Blurring', median) 

Gaussian = cv2.GaussianBlur(img, (7, 7), 0) 
cv2.imshow('Gaussian Blurring', Gaussian) 

bilateral = cv2.bilateralFilter(img, 9, 75, 75) 
cv2.imshow('Bilateral Blurring', bilateral) 

cv2.waitKey(0)

