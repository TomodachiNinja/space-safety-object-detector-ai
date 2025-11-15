from ultralytics import YOLO
import os

def run_inference():
    model_path = 'runs/detect/yash_experiment30/weights/best.pt'
    
    if os.path.exists(model_path):
        model = YOLO(model_path)
        print("Using trained model")
    else:
        print("Trained model not found. Using pre-trained YOLOv8n")
        model = YOLO('yolov8n.pt')
    
    print("Running predictions...")
    model.predict(source='images/val', conf=0.25, save=True)
    
    print("Results saved to runs/detect/predict/")

if __name__ == "__main__":
    run_inference()