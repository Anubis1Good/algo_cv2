import cv2
import numpy as np
img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

median = cv2.medianBlur(img, 7) 

Gaussian = cv2.GaussianBlur(img, (7, 7), 0) 

bilateral = cv2.bilateralFilter(img, 15, 75, 75) 

median = cv2.Canny(median, 150, 255)
Gaussian = cv2.Canny(Gaussian, 150, 255)
bilateral = cv2.Canny(bilateral, 150, 255)


cv2.imshow('Median Blurring', median) 
cv2.imshow('Gaussian Blurring', Gaussian) 
cv2.imshow('Bilateral Blurring', bilateral) 


cv2.waitKey(0)

