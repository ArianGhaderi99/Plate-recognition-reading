from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

results = model("testcar_img.jpg")

img = results[0].plot()

cv2.imwrite("test_output.jpg", img)

print("saved")