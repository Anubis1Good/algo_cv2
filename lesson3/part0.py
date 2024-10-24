import cv2

img = cv2.imread('enot.jpg')
img = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow(str(img.shape),img)
cv2.imshow(str(gray_img.shape),gray_img)
cv2.waitKey(0)