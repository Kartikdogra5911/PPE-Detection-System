import os
import shutil

# Change these paths if needed
prediction_folder = r"C:\Users\dogra\OneDrive\Desktop\PPE_Dataset_v2\runs\detect\predict-4"
labels_folder = os.path.join(prediction_folder, "labels")
output_folder = r"C:\Users\dogra\OneDrive\Desktop\No_Detection_Predict4"

os.makedirs(output_folder, exist_ok=True)

image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

copied = 0
total = 0

for file in os.listdir(prediction_folder):
    if os.path.splitext(file)[1].lower() in image_extensions:
        total += 1
        image_name = os.path.splitext(file)[0]
        label_path = os.path.join(labels_folder, image_name + ".txt")

        if not os.path.exists(label_path):
            shutil.copy2(
                os.path.join(prediction_folder, file),
                os.path.join(output_folder, file)
            )
            copied += 1

print(f"Total Images : {total}")
print(f"No Detection : {copied}")
print("Finished!")