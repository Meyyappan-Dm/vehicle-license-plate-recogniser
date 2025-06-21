# 🚗 Indian License Plate Detection using YOLOv8

A real-time object detection system that identifies **Indian vehicle license plates** using a custom-trained **YOLOv8 model**. This project focuses on accurate **plate detection** in real-world driving scenarios.

---

## 🔍 Features

- ✅ Trained on Indian license plate dataset (Kaggle)
- ✅ Real-time or image-based detection using YOLOv8
- ✅ Lightweight and accurate
- 🚧 (Optional) Extension: OCR for plate text recognition (in progress)

---

## 🧠 Model Architecture

- **Backbone**: YOLOv8
- **Framework**: [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- **Training**: Annotated dataset with bounding boxes around number plates
- **Input**: Images or frames from video/camera
- **Output**: Bounding boxes highlighting license plates

---

## 🗃️ Dataset

- 📦 [Indian Vehicle Number Plate YOLO Annotations (Kaggle)](https://www.kaggle.com/datasets/deepakat002/indian-vehicle-number-plate-yolo-annotation)
- 3,000+ annotated frames from highway videos
- Format: YOLOv5/YOLOv8 format (images + `.txt` labels)
