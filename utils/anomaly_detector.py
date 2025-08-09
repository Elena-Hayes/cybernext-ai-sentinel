import numpy as np

class AnomalyDetector:
    def __init__(self, threshold=5.0):
        self.threshold = threshold

    def is_anomaly(self, data):
        # Simple detection based on sum of values
        return np.sum(data) > self.threshold
