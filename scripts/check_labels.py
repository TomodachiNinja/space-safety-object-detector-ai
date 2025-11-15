import os

def check_labels():
    splits = ['train', 'val', 'test']
    
    for split in splits:
        img_dir = f'images/{split}'
        label_dir = f'labels/{split}'
        
        if not os.path.exists(img_dir):
            continue
            
        print(f"\nChecking {split} split:")
        
        img_files = [f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        if not img_files:
            print(f"  No images found in {img_dir}")
            continue
            
        missing_labels = []
        
        for img_file in img_files:
            label_file = os.path.splitext(img_file)[0] + '.txt'
            label_path = os.path.join(label_dir, label_file)
            
            if not os.path.exists(label_path):
                missing_labels.append(img_file)
        
        if missing_labels:
            print(f"  Missing labels for {len(missing_labels)} images:")
            for img in missing_labels[:5]:
                print(f"    {img}")
            if len(missing_labels) > 5:
                print(f"    ... and {len(missing_labels) - 5} more")
        else:
            print(f"  All {len(img_files)} images have corresponding labels ✓")

if __name__ == "__main__":
    check_labels()