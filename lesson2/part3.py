import pyautogui as pag
import cv2

pag.screenshot('Screen.png')
img = cv2.imread('Screen.png')
img = img[0:700,0:700]
color = (25,168,25)
mask = cv2.inRange(img,color,color)

cv2.imshow('mask',mask)
cv2.imshow('img',img)
cv2.waitKey(0)


