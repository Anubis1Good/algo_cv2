import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Doge.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# функция cvtColor меняет цветовое пространство 
# изображения
# первым параметром указывается изображение,
# вторым цветовое пространство
plt.imshow(img)
plt.show()

