# 🚘 PlateVision

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/YOLOv8-Object%20Detection-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/EasyOCR-OCR-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv">
</p>

<p align="center">
  <b>Deep Learning Based Automatic License Plate Recognition System</b>
</p>

<p align="center">
  Detect license plates with YOLOv8 and extract plate text using EasyOCR.
</p>

---

## 📖 Overview

PlateVision is an end-to-end Automatic License Plate Recognition (ALPR) system developed using modern Deep Learning and Computer Vision techniques.

The project combines:

* YOLOv8 for License Plate Detection
* EasyOCR for Character Recognition
* OpenCV for Image Processing

The system automatically detects license plates in vehicle images and extracts the plate number.

---

## ✨ Features

* 🚗 License Plate Detection
* 🔍 Optical Character Recognition (OCR)
* 🧠 Custom YOLOv8 Training
* ⚡ CPU-Friendly Inference
* 📸 Image-Based Recognition
* 🏷️ Bounding Box Visualization
* 🎯 Confidence-Based Prediction
* 📦 Lightweight and Easy to Run

---

## 🧠 Pipeline

```text
Input Image
      │
      ▼
YOLOv8 Detection
      │
      ▼
License Plate Localization
      │
      ▼
Plate Cropping
      │
      ▼
Grayscale Preprocessing
      │
      ▼
EasyOCR Recognition
      │
      ▼
Detected Plate Number
```

---

## 📸 Model Result

<p align="center">
  <img src="result.jpg" width="900">
</p>

<p align="center">
  <i>License Plate Detection and Recognition Result</i>
</p>

---

## 📂 Dataset

The dataset is not included in this repository because of GitHub file size limitations.

### Download Dataset

Download the dataset from the original source:

DATASET_DOWNLOAD_LINK

After downloading, extract the dataset and place it inside the project directory.

Expected structure:

```text
dataset/
├── train/
│   ├── images/
│   ├── annotations/
│   └── labels/
│
└── val/
    ├── images/
    ├── annotations/
    └── labels/
```

### Convert XML Annotations

The original dataset uses Pascal VOC XML annotations.

Convert annotations to YOLO format:

```bash
python convert.py
```

After conversion:

```text
dataset/
├── train/
│   ├── images/
│   ├── annotations/
│   └── labels/
│
└── val/
    ├── images/
    ├── annotations/
    └── labels/
```

---

## 🏗️ Project Structure

```text
PlateVision/
│
├── dataset/
│
├── runs/
│
├── data.yaml
├── train.py
├── main.py
│
├── requirements.txt
├── yolov8n.pt
│
├── result.jpg
├── testcar_img.jpg
├── testcar_img2.jpg
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/PlateVision.git

cd PlateVision
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

```txt
ultralytics
opencv-python
easyocr
numpy
torch
torchvision
```

---

## 🎯 Training

Train the YOLOv8 model:

```bash
python train.py
```

Training Configuration:

* YOLOv8 Nano
* Custom License Plate Dataset
* CPU Compatible
* Ultralytics Framework

---

## 🔍 Inference

Run License Plate Detection and OCR:

```bash
python main.py
```

Output:

```text
result.jpg
```

The output image contains:

* Detected license plate
* Bounding box
* Recognized plate number

---

## 🛠 Technologies Used

| Technology | Purpose               |
| ---------- | --------------------- |
| YOLOv8     | Object Detection      |
| EasyOCR    | Character Recognition |
| OpenCV     | Image Processing      |
| NumPy      | Numerical Operations  |
| Python     | Development           |
| PyTorch    | Deep Learning Backend |

---

## 📊 Example Output

```text
Plate: GJ03ER0563
```

---

## 🚀 Future Improvements

* 🎥 Video Processing
* 📹 Real-Time Webcam Detection
* 🌍 Multi-Country License Plates
* 🇮🇷 Iranian License Plate Recognition
* 🗄️ Database Integration
* 🌐 Flask/FastAPI Deployment
* 🐳 Docker Support

---

## 🎓 Learning Objectives

This project demonstrates:

* Deep Learning Fundamentals
* Object Detection with YOLOv8
* OCR Integration
* Dataset Preparation
* XML to YOLO Annotation Conversion
* Model Training and Evaluation
* Computer Vision Pipelines

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.

---

## 👨‍💻 Author

Developed as a Deep Learning and Computer Vision project using YOLOv8, EasyOCR, and OpenCV.

---

<p align="center">
  Made with ❤️ using Python, YOLOv8 and Deep Learning
</p>
