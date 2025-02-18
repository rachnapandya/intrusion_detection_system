import os
import json
import time
import numpy as np
from sklearn.ensemble import IsolationForest
from kafka import KafkaConsumer
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO)

# Kafka configuration (update as needed)
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "network-logs")

# Initialize Kafka consumer to listen for network logs
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def extract_features(log):
    """
    Extract features from a network log entry.
    In a real system, you would extract meaningful features from the log data.
    This dummy function assumes the log has 'src_port', 'dst_port', and 'packet_size' fields.
    """
    features = [
        log.get('src_port', 0),
        log.get('dst_port', 0),
        log.get('packet_size', 0)
    ]
    return features

def main():
    logs_buffer = []
    buffer_size = 50  # Process logs in batches
    
    # Initialize Isolation Forest for anomaly detection
    isolation_forest = IsolationForest(contamination=0.1, random_state=42)
    
    logging.info("Starting Intrusion Detection System... Listening on topic '%s'", KAFKA_TOPIC)
    
    while True:
        try:
            for message in consumer:
                log_entry = message.value
                logs_buffer.append(log_entry)
                
                if len(logs_buffer) >= buffer_size:
                    # Extract features from each log in the batch
                    X = np.array([extract_features(log) for log in logs_buffer])
                    
                    # Fit the Isolation Forest model and predict anomalies
                    if len(X) > 0:
                        isolation_forest.fit(X)
                        predictions = isolation_forest.predict(X)
                        
                        # Log any anomalies detected
                        for log_data, pred in zip(logs_buffer, predictions):
                            if pred == -1:
                                logging.warning("Anomaly detected: %s", log_data)
                                # In production, forward anomaly to ELK or alerting system.
                    
                    # Clear the buffer after processing
                    logs_buffer = []
        except Exception as e:
            logging.error("Error while processing logs: %s", e)
            time.sleep(1)

if __name__ == "__main__":
    main()
