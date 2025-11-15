import os
import numpy as np
from PIL import Image, ImageDraw
import random

def create_sample_data():
    splits = {'train': 10, 'val': 3}
    
    for split, count in splits.items():
        img_dir = f'images/{split}'
        label_dir = f'labels/{split}'
        
        os.makedirs(img_dir, exist_ok=True)
        os.makedirs(label_dir, exist_ok=True)
        
        for i in range(count):
            img = Image.new('RGB', (640, 640), color=(100, 150, 200))
            draw = ImageDraw.Draw(img)
            
            objects = []
            num_objects = random.randint(1, 3)
            
            for _ in range(num_objects):
                class_id = random.randint(0, 79)
                x = random.randint(50, 590)
                y = random.randint(50, 590)
                w = random.randint(30, 100)
                h = random.randint(30, 100)
                
                color = [(255,0,0), (0,255,0), (0,0,255)][class_id % 3]
                draw.rectangle([x, y, x+w, y+h], outline=color, width=3)
                
                x_center = (x + w/2) / 640
                y_center = (y + h/2) / 640
                width = w / 640
                height = h / 640
                
                objects.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
            
            img_path = f'{img_dir}/sample_{i:03d}.jpg'
            img.save(img_path)
            
            label_path = f'{label_dir}/sample_{i:03d}.txt'
            with open(label_path, 'w') as f:
                f.write('\n'.join(objects))
        
        print(f"Created {count} sample images in {split} split")

if __name__ == "__main__":
    create_sample_data()