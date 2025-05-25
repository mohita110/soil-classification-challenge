#!/bin/bash
set -e

# ---- Soil Dataset Download ----
KAGGLE_DATASET="annam-ai/soilclassification-part2"
TARGET_DIR="./data"

echo "Downloading dataset: $KAGGLE_DATASET"
mkdir -p "$TARGET_DIR"
kaggle datasets download -d "$KAGGLE_DATASET" -p "$TARGET_DIR" --unzip

echo "Download complete. Files saved to $TARGET_DIR"
# ---not soil - cifar 10 ---Download
pip install --quiet gdown

GDRIVE_FOLDER_ID="1H95RE3o0j1n50yj3MSvRSCEVZKN9jH-G"
gdown --folder "https://drive.google.com/drive/folders/1H95RE3o0j1n50yj3MSvRSCEVZKN9jH-G?usp=sharing" -O data/not-soil



echo "All downloads completed."
