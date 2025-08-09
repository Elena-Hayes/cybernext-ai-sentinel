import argparse
import yaml
from utils.logger import Logger
from utils.anomaly_detector import AnomalyDetector

def main(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    logger = Logger(config['logging']['log_file'])
    detector = AnomalyDetector(threshold=config['detection']['threshold'])

    logger.log("Starting AI Sentinel anomaly detection...")
    # Simulate some input data for anomaly detection
    test_data = [[0.1, 0.2, 0.3], [10, 12, 9], [0.05, 0.04, 0.07]]
    for i, data in enumerate(test_data):
        if detector.is_anomaly(data):
            logger.log(f"Anomaly detected in packet #{i+1}: {data}")
        else:
            logger.log(f"Packet #{i+1} is normal.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CyberNext AI Sentinel")
    parser.add_argument("--config", type=str, required=True, help="Path to YAML config file")
    args = parser.parse_args()

    main(args.config)
