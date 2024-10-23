import pyautogui as pag
import cv2
import numpy as np

pag.screenshot('Screen.png')
img = cv2.imread('Screen.png')
img = img[0:700,0:700]
color = (25,168,25)
mask = cv2.inRange(img,color,color)

cords = np.argwhere(mask == 255)
pag.click(cords[0][1],cords[0][0])


