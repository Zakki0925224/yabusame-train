from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(
    data="project-3-at-2025-01-16-07-57-578a93f1.yaml",
    epochs=50,
    imgsz=640,
    device="cpu",
)
model.export(format="tflite")
