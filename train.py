from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(
    data="data.yaml",
    epochs=20,
    imgsz=640,
    batch=8,
    workers=0,
    device="cpu",
    project="runs",
    name="license_plate"
)