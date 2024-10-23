import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Doge.jpg')

red = img[:,:,2]
img[:,:,2] = img[:,:,0]
img[:,:,0] = red

# тоже самое можно сделать
# путем работы с numpy
plt.imshow(img)
plt.show()
