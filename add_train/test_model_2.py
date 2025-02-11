import cv2
from ultralytics import YOLO
video_path = "video5210877966749291300.mp4"
cap = cv2.VideoCapture(video_path)
model = YOLO('runs\detect\\red5\weights\\best.pt')
# Получение FPS видео
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Настройка VideoWriter для сохранения выходного видео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('out_'+video_path, fourcc, fps, (width, height))

while True:
    # Считывание кадра из видео
    ret, frame = cap.read()
    if not ret:
        break
    res = model(frame)[0]
    annotated_frame = res.plot()
    out.write(annotated_frame)

    if cv2.waitKey(1) == 27:
        break
# Освобождение видеозахвата и закрытие всех окон OpenCV
cap.release()
out.release()  # закрытие выходного видеофайла
cv2.destroyAllWindows()