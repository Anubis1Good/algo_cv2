import cv2

cap = cv2.VideoCapture('Апельсины.mp4')

while True:
    ret, frame = cap.read()
    cv2.imshow('video orange', frame)
    if cv2.waitKey(33) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

