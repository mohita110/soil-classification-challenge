"""

Author: Annam.ai IIT Ropar
Team Name: TeamZirconia
Team Members: Mohita, Siya Kumar
Leaderboard Rank: <72>

"""

# preprocessing.py

from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

def preprocess_image(img_path, target_size=(224, 224)):
    """
    Load an image file, resize to target size, and normalize pixel values to [0,1].
    Returns a numpy array with batch dimension.
    """
    img = load_img(img_path, target_size=target_size)
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array
