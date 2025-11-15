# My YOLO Project (template)

This is a ready-to-use template for training YOLOv8 with the `ultralytics` package.

## Structure
```
/mnt/data/my_yolo_project
├─ images/
│  ├─ train/        # put training images (.jpg/.png)
│  ├─ val/          # put validation images
│  └─ test/         # optional
├─ labels/
│  ├─ train/        # corresponding .txt (YOLO format)
│  ├─ val/
│  └─ test/
├─ data.yaml        # dataset config (edit class names here)
├─ train.py         # training script using ultralytics YOLO API
├─ requirements.txt # pip install -r requirements.txt
└─ scripts/
   └─ check_labels.py # utility to check missing labels
```

## Quick start (commands to run in terminal)

1. create & activate virtual env (optional but recommended)
```bash
python -m venv venv
# windows
venv\Scripts\activate
# mac/linux
source venv/bin/activate
```

2. install requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Put your images in `images/train` and `images/val` and corresponding `.txt` labels in `labels/train` and `labels/val`.
   Label format (YOLO): `class_id x_center y_center width height` (all normalized between 0 and 1).

4. Edit `data.yaml` to match your class names.

5. (Optional) run the label check script to spot missing labels:
```bash
python scripts/check_labels.py
```

6. Start training:
```bash
python train.py
```
or using CLI:
```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=30 imgsz=640 batch=8 name=yash_experiment
```

## After training
Check `runs/detect/yash_experiment/weights/` for `best.pt` and `last.pt`.
Use these for inference or further validation:
```python
from ultralytics import YOLO
model = YOLO('runs/detect/yash_experiment/weights/best.pt')
model.val()
model.predict(source='images/test', conf=0.25, save=True)
```


