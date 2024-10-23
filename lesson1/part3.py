import cv2

img = cv2.imread('Doge.jpg')
cv2.imshow('some img',img[:,:,1])

cv2.waitKey(0)