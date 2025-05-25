#!/bin/bash

# Dataset or competition or notebook slug
# dataset: 'soil-classification'
# competition: 'soil-classification'
# notebook: 'mohita/soil_classification'

# === Download a dataset ===
KAGGLE_DATASET="soilclassification-part2"
TARGET_DIR="./data"

echo "Downloading dataset: $KAGGLE_DATASET"
mkdir -p "$TARGET_DIR"
kaggle competitions download -c "$KAGGLE_COMPETITION" -p "$TARGET_DIR" --unzip

echo "Download complete. Files saved to $TARGET_DIR"
