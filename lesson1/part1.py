import cv2 # импорт cv2

img = cv2.imread('Doge.jpg') # чтение изображения

cv2.imshow('some img',img) # отображение изображения

cv2.waitKey(0) # ждем действия пользователя для завершения работы программы

print(type(img))