from ultralytics import YOLO
import cv2
import numpy as np
# Загрузка модели YOLOv8-Pose
model = YOLO('models/yolov8n-pose.pt')
# Словарь цветов для различных классов
colors = {
    'white': (255, 255, 255),
    'red': (0, 0, 255),
    'blue': (255, 0, 0)
}
def draw_skeleton(image, keypoints, confs, pairs, color):
    for (start, end) in pairs:
        if confs[start] > 0.5 and confs[end] > 0.5:
            x1, y1 = int(keypoints[start][0]), int(keypoints[start][1])
            x2, y2 = int(keypoints[end][0]), int(keypoints[end][1])
            if (x1, y1) != (0, 0) and (x2, y2) != (0, 0):  # Игнорирование точек в (0, 0)
                cv2.line(image, (x1, y1), (x2, y2), color, 2)

def process_image(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)
    # Обработка изображения с помощью модели
    results = model(image)[0]
    # Обработка ключевых точек
    if results.keypoints:
        keypoints = results.keypoints.data.cpu().numpy()
        confs = results.keypoints.conf.cpu().numpy()
    
        for i, (kp, conf) in enumerate(zip( keypoints, confs)):
            # Визуализация ключевых точек с номерами
            for j, (point, point_conf) in enumerate(zip(kp, conf)):
                if point_conf > 0.5:  # Фильтрация по уверенности
                    x, y = int(point[0]), int(point[1])
                    if (x, y) != (0, 0):  # Игнорирование точек в (0, 0)
                        cv2.circle(image, (x, y), 5, colors['blue'], -1)
                        cv2.putText(image, str(j), (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, colors['blue'], 2)
            # Рисование скелета
            draw_skeleton(image, kp, conf, [(5, 7), (7, 9), (6, 8), (8, 10)], colors['white']) # Руки
            draw_skeleton(image, kp, conf, [(11, 13), (13, 15), (12, 14), (14, 16)], colors['red']) # Ноги
            draw_skeleton(image, kp, conf, [(5, 11), (6, 12)], colors['blue']) # Тело

    # Сохранение и отображение результатов
    output_path = "pose_detected_"+image_path
    cv2.imwrite(output_path, image)

# Путь к изображению для обработки
image_path = 'IronMan.jpg'
process_image(image_path)

