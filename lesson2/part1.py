import cv2
import numpy as np

img = np.zeros((400,600,3),dtype=np.uint8)

cv2.line(img, (50,50),(100,200),(255,255,255),5)

pts = np.array([[100,50],[200,300],[500,200],[500,100]])
cv2.polylines(img,[pts],False,(0,255,255))

cv2.circle(img,(200,200),30,(200,200,0),3)
cv2.ellipse(img,(350,300),(100,50),0,0,180,255,-1)
cv2.rectangle(img,(250,100),(410,200),(0,255,0),3)

cv2.imshow('black',img)

cv2.waitKey(0)
