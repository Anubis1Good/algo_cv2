import cv2
import numpy as np
img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

edges = cv2.Canny(thresh, 150, 255)


cv2.imshow('canny',edges)

cv2.waitKey(0)

