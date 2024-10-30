import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# image_path = 'Hogwarts_express.png'
image_path = 'algo.png'
img = cv2.imread(image_path)
reader = easyocr.Reader(['ru'], gpu=False)
text_ = reader.readtext(img)
threshold = 0.80

for t_, t in enumerate(text_):
    print(t)
    bbox, text, score = t
    bbox = np.array(bbox,dtype=np.int32)
    if score > threshold:
        cv2.polylines(img, [bbox],True, (0, 255, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

