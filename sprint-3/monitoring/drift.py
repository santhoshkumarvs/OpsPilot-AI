import numpy as np
from scipy.stats import entropy

def calculate_psi(expected, actual, buckets=10):
    breakpoints = np.percentile(expected, np.linspace(0, 100, buckets + 1))
    expected_counts = np.histogram(expected, bins=breakpoints)[0] + 1e-5
    actual_counts = np.histogram(actual, bins=breakpoints)[0] + 1e-5
    expected_percents = expected_counts / expected_counts.sum()
    actual_percents = actual_counts / actual_counts.sum()
    psi_value = np.sum((expected_percents - actual_percents) * np.log(expected_percents / actual_percents))
    return psi_value

def check_drift(reference_data, current_data, threshold=0.1):
    psi = calculate_psi(reference_data, current_data)
    return {
        "drift_detected": psi > threshold,
        "details": f"PSI={psi:.4f}, threshold={threshold}"
    }
