from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(
    data="project-3-at-2025-01-06-09-00-68834e25.yaml",
    epochs=50,
    imgsz=640,
    device="cpu",
)
model.export(format="tflite")
