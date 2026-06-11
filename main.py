from ultralytics import YOLO
import cv2
import easyocr

# Load YOLO model
model = YOLO("runs\\detect\\runs\\license_plate\\weights\\best.pt")

# Load OCR
reader = easyocr.Reader(
    ['en'],
    gpu=False
)

# Read image
image = cv2.imread("testcar_img2.jpg")

if image is None:
    raise Exception("Image not found!")

# Detect plates
results = model(
    image,
    conf=0.25
)

for box in results[0].boxes:

    x1, y1, x2, y2 = map(
        int,
        box.xyxy[0]
    )

    plate = image[y1:y2, x1:x2]

    if plate.size == 0:
        continue

    # Upscale plate
    plate = cv2.resize(
        plate,
        None,
        fx=4,
        fy=4,
        interpolation=cv2.INTER_CUBIC
    )

    # Simple grayscale
    gray = cv2.cvtColor(
        plate,
        cv2.COLOR_BGR2GRAY
    )

    # OCR
    ocr_results = reader.readtext(
        gray,
        allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        paragraph=False
    )

    plate_text = ""

    if ocr_results:
        best = max(
            ocr_results,
            key=lambda x: x[2]
        )

        plate_text = best[1]

    print("Plate:", plate_text)

    # Draw box
    cv2.rectangle(
        image,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2
    )

    # Draw text
    cv2.putText(
        image,
        plate_text,
        (x1, max(y1 - 10, 20)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

# Save only final image
cv2.imwrite(
    "result.jpg",
    image
)

print("Done! Saved as result.jpg")