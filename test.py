from ultralytics import YOLO

# Load your trained model
model = YOLO("bestv4.pt")   # Replace with your model path

# Run prediction on an image
results = model("input.jpg")   # Replace with your image path

# Print results
print(results)

# Save predicted image
results[0].save("output.jpg")

print("Prediction completed!")
print("Output image saved as output.jpg")