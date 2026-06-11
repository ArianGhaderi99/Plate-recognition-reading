from ultralytics import YOLO

model = YOLO("runs\\detect\\runs\\license_plate\\weights\\best.pt")

results = model(
    "testcar_img.jpg",
    save=True,
    conf=0.3
)