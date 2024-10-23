import cv2

img = cv2.imread('Doge.jpg')
img = cv2.resize(img,(400, 300))
cv2.imshow('some img',img)

cv2.waitKey(0)
