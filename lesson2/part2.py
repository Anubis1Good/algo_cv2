import cv2

img = cv2.imread('Cat1.jpg')

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'не переживай',(150,100), font, 3,(255,255,255),2)
cv2.putText(img,'скоро мы начнем',(80,700), font, 3,(255,255,255),2)
cv2.putText(img,'искать объекты',(120,780), font, 3,(255,255,255),2)

cv2.imshow('Cat',img)
cv2.waitKey(0)

