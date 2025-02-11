from ultralytics import YOLO
import cv2
import os
model = YOLO('runs\detect\\red5\weights\\best.pt')

# img = cv2.imread('images\\test\\5453902107464813652.jpg')
imgs = os.listdir('cats_tast')
for i,img in enumerate(imgs):
    res = model('cats_tast/'+img)[0]
    annotated_frame = res.plot()
    annotated_frame = cv2.resize(annotated_frame, (annotated_frame.shape[1]//2,annotated_frame.shape[0]//2))
    cv2.imshow(str(i),annotated_frame)
cv2.waitKey(0)