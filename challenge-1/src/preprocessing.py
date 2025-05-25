"""

Author: Annam.ai IIT Ropar
Team Name: TeamZirconia
Team Members: Mohita, Siya Kumar
Leaderboard Rank: <140>

"""

# This code is to categorize the given images in train folder according to the csv file of train.csv given into Alluvial, Black, Clay and Red soil folder.

from google.colab import files
import zipfile
import pandas as pd
import os
from shutil import copy2
from glob import glob

# === Step 1: Upload train.zip ===
print("📁 Upload your 'train.zip' file (images):")
uploaded_zip = files.upload()
zip_filename = next((f for f in uploaded_zip.keys() if f.endswith('.zip')), None)
if not zip_filename:
    raise ValueError("❌ You must upload a .zip file!")

# Extract to train_images/
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall('train_images')
print("✅ Images extracted!")

# === Step 2: Upload CSV file ===
print("\n📄 Upload your CSV file (image_id and soil_type):")
uploaded_csv = files.upload()
csv_filename = next((f for f in uploaded_csv.keys() if f.endswith('.csv')), None)
if not csv_filename:
    raise ValueError("❌ You must upload a .csv file!")

df = pd.read_csv(csv_filename)
print("✅ CSV loaded!")

# === Step 3: Build a map of all image files (regardless of extension/case) ===
image_files = glob('train_images/**/*.*', recursive=True)
image_map = {os.path.splitext(os.path.basename(f))[0].lower(): f for f in image_files}

# === Step 4: Organize images into folders by soil_type ===
output_dir = 'sorted_images'
os.makedirs(output_dir, exist_ok=True)

missing_images = []

for _, row in df.iterrows():
    img_id_raw = row['image_id']
    img_id = os.path.splitext(img_id_raw)[0].lower()
    soil_type = row['soil_type']

    dest_folder = os.path.join(output_dir, soil_type)
    os.makedirs(dest_folder, exist_ok=True)

    if img_id in image_map:
        src_path = image_map[img_id]
        dest_path = os.path.join(dest_folder, os.path.basename(src_path))
        copy2(src_path, dest_path)
    else:
        missing_images.append(img_id_raw)
        print(f"⚠️ Warning: Image {img_id_raw} not found!")

# === Step 5: Zip the sorted folder ===
output_zip = 'soil_type_sorted_images.zip'
with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk(output_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            arcname = os.path.relpath(file_path, output_dir)
            zipf.write(file_path, arcname)

# === Step 6: Download final ZIP ===
files.download(output_zip)
print(f"\n✅ Done! Missing images: {len(missing_images)}. Download available.")

