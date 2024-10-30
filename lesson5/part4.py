import cv2
import numpy as np
from ultralytics import YOLO
model = YOLO('models/yolov8n.pt')
cap = cv2.VideoCapture('Апельсины.mp4')

colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),
    (255, 0, 255), (192, 192, 192), (128, 128, 128), (128, 0, 0), (128, 128, 0),
    (0, 128, 0), (128, 0, 128), (0, 128, 128), (0, 0, 128), (72, 61, 139),
    (47, 79, 79), (47, 79, 47), (0, 206, 209), (148, 0, 211), (255, 20, 147)
]
# Функция для обработки изображения
def process_image(image):
    # Загрузка изображения
    results = model(image)[0]
    # Получение результатов
    classes_names = results.names
    classes = results.boxes.cls.cpu().numpy()
    boxes = results.boxes.xyxy.cpu().numpy().astype(np.int32)
    # Рисование рамок
    for class_id, box in zip(classes, boxes):
        class_name = classes_names[int(class_id)]
        color = colors[int(class_id) % len(colors)]  # Выбор цвета для класса
        # Рисование рамок на изображении
        x1, y1, x2, y2 = box
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        cv2.putText(image, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

while True:
    ret, frame = cap.read()
    process_image(frame)
    cv2.imshow('video orange', frame)
    if cv2.waitKey(33) == 27:
        break
cap.release()
cv2.destroyAllWindows()

