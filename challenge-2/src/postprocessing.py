"""

Author: Annam.ai IIT Ropar
Team Name: TeamZirconia
Team Members: Mohita, Siya Kumar
Leaderboard Rank: <72>

"""


# postprocessing.py

def threshold_prediction(prediction, threshold=0.5):
    """
    Converts a probability prediction to binary label.
    If prediction > threshold, label=1 else 0.
    """
    return 1 if prediction > threshold else 0

def format_results(filename, prediction, probability, threshold=0.5):
    """
    Format output dictionary for predictions.
    """
    label = str(threshold_prediction(probability, threshold))
    return {"filename": filename, "prediction": label, "probability": float(probability)}

# Optional: placeholder for evaluation if labels available
def evaluate_predictions(y_true, y_pred):
    """
    Evaluate predictions using F1-score or other metrics if ground truth available.
    """
    from sklearn.metrics import f1_score
    return f1_score(y_true, y_pred)
