import cv2
import numpy as np
from deepface import DeepFace

img1_path = "faces\RG1.jpg"
img2_path = "faces\\NRG3.jpg"

result = DeepFace.verify(img1_path,img2_path)

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

w = max(img1.shape[1],img2.shape[1])//2
h = max(img1.shape[0],img2.shape[0])//2

img1 = cv2.resize(img1,(w,h))
img2 = cv2.resize(img2,(w,h))
img = np.zeros((h+100,w*2,3),np.uint8)
img[:h,:w] = img1
img[:h,w:] = img2
cv2.putText(img,'verified: '+str(result['verified']),(w-100,h+50),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)

