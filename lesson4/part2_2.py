import cv2
import numpy as np
from ultralytics import YOLO
model = YOLO('models/yolov8n-seg.pt')
# Цвет для выделения объектов класса "person"
person_color = (0, 255, 0)  # Зеленый цвет

def process_image(image_path):
    frame = cv2.imread(image_path)
    image_orig = frame.copy()
    h_or, w_or = frame.shape[:2]
    image = cv2.resize(frame, (640, 640))
    results = model(image)[0]
    classes = results.boxes.cls.cpu().numpy()
    masks = results.masks.data.cpu().numpy()
    # Создаем зеленый фон
    green_background = np.zeros_like(image_orig)
    green_background[:] = person_color
    # Наложение масок на изображение
    for i, mask in enumerate(masks):
        class_name = results.names[int(classes[i])]
        if class_name == 'person':
            color_mask = np.zeros((640, 640, 3), dtype=np.uint8)
            resized_mask = cv2.resize(mask, (640, 640), interpolation=cv2.INTER_NEAREST)
            color_mask[resized_mask > 0] = person_color
            color_mask = cv2.resize(color_mask, (w_or, h_or), interpolation=cv2.INTER_NEAREST)
            mask_resized = cv2.resize(mask, (w_or, h_or), interpolation=cv2.INTER_NEAREST)
            green_background[mask_resized > 0] = image_orig[mask_resized > 0]
    output_path = "removed_BG"+image_path
    cv2.imwrite(output_path, green_background)

# Путь к изображению, которое необходимо обработать
image_path = 'Boromir.jpg'
process_image(image_path)

