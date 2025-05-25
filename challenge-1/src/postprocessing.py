"""

Author: Annam.ai IIT Ropar
Team Name: TeamZirconia
Team Members: Mohita, Siya Kumar
Leaderboard Rank: <140>

"""

# Here you add all the post-processing related details for the task completed from Kaggle.

import os
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from zipfile import ZipFile
from google.colab import files

# Step 1: Upload and extract test data
print("Please upload your test.zip file")
uploaded = files.upload()
test_zip_name = next(iter(uploaded))

# Extract test images
test_dir = '/content/test_images'
os.makedirs(test_dir, exist_ok=True)
with ZipFile(test_zip_name, 'r') as zip_ref:
    zip_ref.extractall(test_dir)
print("Test images extracted!")

# Load the trained model
model = load_model('soil_classifier.keras')

# Get class names from training (assuming same order)
class_names = ['Alluvial', 'Black', 'Clay', 'Red']  # Adjust if different

# Process test images and make predictions
results = []
for img_file in os.listdir(test_dir):
    if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Load and preprocess image
        img_path = os.path.join(test_dir, img_file)
        img = image.load_img(img_path, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Make prediction
        preds = model.predict(img_array)
        predicted_class = class_names[np.argmax(preds)]
        confidence = np.max(preds)

        # Store results
        results.append({
            'Image': img_file,
            'Predicted_Class': predicted_class,
            'Confidence': float(confidence)
        })

# Create and save CSV
df = pd.DataFrame(results)
csv_filename = 'soil_predictions.csv'
df.to_csv(csv_filename, index=False)
print(f"\nPredictions saved to {csv_filename}")

# Display the results
print("\nPrediction Results:")
print(df.to_string(index=False))

# Download the CSV file
files.download(csv_filename)
