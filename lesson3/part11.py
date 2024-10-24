import cv2
import numpy as np

# img = cv2.imread('peoples.png')
img = cv2.imread('avengers_cover.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("cascades\haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(img_gray)
for x, y, width, height in faces:
    cv2.rectangle(img, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=5)
img = cv2.resize(img,(img.shape[1]//3,img.shape[0]//3))
cv2.imshow('img',img)
cv2.waitKey(0)