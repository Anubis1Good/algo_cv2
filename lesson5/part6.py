from collections import defaultdict
import cv2
import numpy as np
from ultralytics import YOLO

# Загрузка модели YOLOv8
model = YOLO("models/yolov8n.pt")

# Открытие видео файла
video_path = "soccer.mp4"
cap = cv2.VideoCapture(video_path)

# Получение FPS видео
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Настройка VideoWriter для сохранения выходного видео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('out_'+video_path, fourcc, fps, (width, height))

# Создание словаря для хранения истории треков объектов
track_history = defaultdict(list)

# Цикл для обработки каждого кадра видео
while True:
    # Считывание кадра из видео
    ret, frame = cap.read()
    # Закрываем, если видео закончилось.
    if not ret:
        break
    # Применение YOLOv8 для отслеживания объектов на кадре, с сохранением треков между кадрами
    results = model.track(frame, persist=True)
    # Проверка на наличие объектов
    if results[0].boxes is not None and results[0].boxes.id is not None:
        # Получение координат боксов и идентификаторов треков
        boxes = results[0].boxes.xywh.cpu()  # xywh координаты боксов
        track_ids = results[0].boxes.id.int().cpu().tolist()  # идентификаторы треков
        # Визуализация результатов на кадре
        annotated_frame = results[0].plot()
        # Отрисовка треков
        for box, track_id in zip(boxes, track_ids):
            x, y, w, h = box  # координаты центра и размеры бокса
            track = track_history[track_id]
            track.append((float(x), float(y)))  # добавление координат центра объекта в историю
            if len(track) > 30:  # ограничение длины истории до 30 кадров
                track.pop(0)
            # Рисование линий трека
            points = np.hstack(track).astype(np.int32).reshape((-1, 2))
            cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=10)
        # Отображение аннотированного кадра
        cv2.imshow("YOLOv8 Tracking", annotated_frame)
        out.write(annotated_frame)  # запись кадра в выходное видео
    else:
        # Если объекты не обнаружены, просто отображаем кадр
        cv2.imshow("YOLOv8 Tracking", frame)
        out.write(frame)  # запись кадра в выходное видео
    # Прерывание цикла при нажатии клавиши 'Esc'
    if cv2.waitKey(1) == 27:
        break
# Освобождение видеозахвата и закрытие всех окон OpenCV
cap.release()
out.release()  # закрытие выходного видеофайла
cv2.destroyAllWindows()