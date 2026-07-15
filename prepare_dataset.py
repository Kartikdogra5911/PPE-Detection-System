import os
import random
import shutil
from pathlib import Path



MASTER_DATASET = r"C:\Users\dogra\OneDrive\Desktop\PPE_Models\Master Dataset"
OUTPUT_DATASET = r"C:\Users\dogra\OneDrive\Desktop\PPE_Dataset_v2"

TRAIN_RATIO = 0.70
VALID_RATIO = 0.20
TEST_RATIO = 0.10

CLASS_NAMES = [
    "helmet",
    "vest"
]

RANDOM_SEED = 42


random.seed(RANDOM_SEED)

master = Path(MASTER_DATASET)
output = Path(OUTPUT_DATASET)

images_dir = master / "images"
labels_dir = master / "labels"

# Create folders
for split in ["train", "valid", "test"]:
    (output / split / "images").mkdir(parents=True, exist_ok=True)
    (output / split / "labels").mkdir(parents=True, exist_ok=True)

# Collect valid image-label pairs
pairs = []

image_extensions = [".jpg", ".jpeg", ".png"]

for img in images_dir.iterdir():

    if img.suffix.lower() not in image_extensions:
        continue

    label = labels_dir / (img.stem + ".txt")

    if label.exists():
        pairs.append((img, label))

print(f"\nValid image-label pairs : {len(pairs)}")

random.shuffle(pairs)

total = len(pairs)

train_end = int(total * TRAIN_RATIO)
valid_end = train_end + int(total * VALID_RATIO)

train = pairs[:train_end]
valid = pairs[train_end:valid_end]
test = pairs[valid_end:]

dataset = {
    "train": train,
    "valid": valid,
    "test": test
}

# Copy files
for split, files in dataset.items():

    for img, lbl in files:

        shutil.copy2(
            img,
            output / split / "images" / img.name
        )

        shutil.copy2(
            lbl,
            output / split / "labels" / lbl.name
        )

# Create data.yaml

yaml_path = output / "data.yaml"

with open(yaml_path, "w") as f:

    f.write(f"path: {OUTPUT_DATASET.replace(chr(92), '/')}\n\n")

    f.write("train: train/images\n")
    f.write("val: valid/images\n")
    f.write("test: test/images\n\n")

    f.write("names:\n")

    for i, cls in enumerate(CLASS_NAMES):
        f.write(f"  {i}: {cls}\n")

print("\n==============================")
print("DATASET CREATED SUCCESSFULLY")
print("==============================")
print(f"Train : {len(train)}")
print(f"Valid : {len(valid)}")
print(f"Test  : {len(test)}")
print(f"\nSaved to:\n{OUTPUT_DATASET}")
print("==============================")