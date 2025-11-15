# 🎯 YOLOv8 Object Detection Template

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-ultralytics-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**🚀 Ready-to-use template for training YOLOv8 models with the `ultralytics` package**

</div>

---

## 📁 Project Structure

```
📦 object-detection-model
├── 🖼️ images/
│   ├── 🏋️ train/          # Training images (.jpg/.png)
│   ├── ✅ val/            # Validation images
│   └── 🧪 test/           # Test images (optional)
├── 🏷️ labels/
│   ├── 🏋️ train/          # Training labels (.txt YOLO format)
│   ├── ✅ val/            # Validation labels
│   └── 🧪 test/           # Test labels
├── ⚙️ data.yaml           # Dataset configuration
├── 🐍 train.py            # Training script
├── 📋 requirements.txt    # Dependencies
└── 🛠️ scripts/
    └── 🔍 check_labels.py # Label validation utility
```

## 🚀 Quick Start

### 1️⃣ Setup Environment

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3️⃣ Prepare Dataset

> 📝 **Label Format (YOLO):** `class_id x_center y_center width height`  
> All values normalized between 0 and 1

- Place training images in `images/train/`
- Place validation images in `images/val/`
- Add corresponding labels in `labels/train/` and `labels/val/`

### 4️⃣ Configure Dataset

Edit `data.yaml` to match your class names:

```yaml
path: ./
train: images/train
val: images/val
test: images/test

names:
  0: person
  1: car
  # Add your classes here
```

### 5️⃣ Validate Labels (Optional)

```bash
python scripts/check_labels.py
```

### 6️⃣ Start Training

**Option A: Using Python script**
```bash
python train.py
```

**Option B: Using CLI**
```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=30 imgsz=640 batch=8 name=yash_experiment
```

## 🎉 After Training

### 📊 Model Weights
Find your trained models in:
```
runs/detect/yash_experiment/weights/
├── best.pt    # Best performing model
└── last.pt    # Latest checkpoint
```

### 🔮 Inference & Validation

```python
from ultralytics import YOLO

# Load trained model
model = YOLO('runs/detect/yash_experiment/weights/best.pt')

# Validate model
model.val()

# Run predictions
model.predict(source='images/test', conf=0.25, save=True)
```

---

<div align="center">

**⭐ Star this repo if it helped you! ⭐**

</div>


