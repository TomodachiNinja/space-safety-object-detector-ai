from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8n.pt')
    model.predict(source='images/val', conf=0.25, save=True)
    print("Detection complete! Check runs/detect/predict/ for results")