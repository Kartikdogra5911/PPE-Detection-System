from pathlib import Path
import shutil

# =====================================================
# Base YOLO prediction directory
# =====================================================
base_folder = Path(r"C:\Users\dogra\OneDrive\Desktop\PPE_Dataset_v2\runs\detect")

# =====================================================
# Find the latest prediction folder automatically
# =====================================================
predict_folders = [f for f in base_folder.iterdir()
                   if f.is_dir() and f.name.startswith("predict")]

if not predict_folders:
    print("❌ No prediction folders found.")
    exit()

latest_predict = max(predict_folders, key=lambda x: x.stat().st_mtime)

print(f"\nUsing prediction folder:")
print(latest_predict)

labels_folder = latest_predict / "labels"

if not labels_folder.exists():
    print("\n❌ labels folder not found!")
    exit()

output_folder = latest_predict / "No_Detection"
output_folder.mkdir(exist_ok=True)

image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

count = 0

for image in latest_predict.iterdir():

    if image.suffix.lower() not in image_extensions:
        continue

    label_file = labels_folder / (image.stem + ".txt")

    # No label file
    if not label_file.exists():
        shutil.copy2(image, output_folder / image.name)
        print(f"Copied (No Label): {image.name}")
        count += 1
        continue

    # Empty label file
    if label_file.stat().st_size == 0:
        shutil.copy2(image, output_folder / image.name)
        print(f"Copied (Empty Label): {image.name}")
        count += 1

print("\n========================================")
print(f"Total Images with NO Detection : {count}")
print(f"Saved in : {output_folder}")
print("========================================")