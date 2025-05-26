# core/alert_loader.py

import json
import os

def load_alerts(file_path="alerts/simulated_alerts.json"):
    """
    Load alerts from a JSON file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Alert file not found: {file_path}")

    with open(file_path, "r") as f:
        alerts = json.load(f)
    return alerts
