import datetime

class Logger:
    def __init__(self, filepath):
        self.filepath = filepath

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filepath, "a") as f:
            f.write(f"[{timestamp}] {message}\n")
