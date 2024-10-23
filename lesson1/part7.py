import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('Doge.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

mask = np.ones((70,250,3))
img[200:270,470:720] = mask

plt.imshow(img)
plt.show()

img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
cv2.imwrite('Anon.jpg',img)