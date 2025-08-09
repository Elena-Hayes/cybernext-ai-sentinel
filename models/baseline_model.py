class BaselineModel:
    def __init__(self):
        self.mean = None

    def train(self, data):
        self.mean = sum(sum(row) for row in data) / len(data)

    def predict(self, sample):
        return sum(sample) > self.mean
