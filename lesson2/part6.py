import cv2
import numpy as np

img = cv2.imread('oranges.jpg')
color1 = (17,99,176)
color2 = (43,175,250)
mask = cv2.inRange(img,color1,color2)

cv2.imshow('mask',mask)
cv2.imshow('img',img)
cv2.waitKey(0)