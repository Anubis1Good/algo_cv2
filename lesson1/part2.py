import cv2

img = cv2.imread('Doge.jpg')

print(img.shape)

img = img[20:550,450:700]
cv2.imshow('some img',img)

cv2.waitKey(0)

