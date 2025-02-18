

# AI-Powered Intrusion Detection System

![Intrusion Detection Banner](https://via.placeholder.com/1200x300?text=Intrusion+Detection+System)

## Overview
The AI-Powered Intrusion Detection System monitors network traffic in real-time and uses machine learning to detect anomalies. Leveraging Kafka for log streaming and Isolation Forest for anomaly detection, this project aims to provide proactive security insights and alerts.

## Features
- **Real-Time Log Streaming:** Captures network logs via Kafka.
- **Anomaly Detection:** Utilizes Isolation Forest to identify unusual patterns in network traffic.
- **Batch Processing:** Processes logs in batches to improve detection efficiency.
- **Alerting System:** Logs and warns about potential intrusions for further analysis.

## Environment Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/intrusion_detection_system.git
   cd intrusion_detection_system
2. **Setup a virutal Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install Dependecies:**
   ```bash
   pip install -r requirements.txt
4. **Configure Environment Variables:**
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   export PINECONE_API_KEY=your_pinecone_api_key
   export PINECONE_ENV=your_pinecone_env
5. **Configure Kafka Settings:
   Update the `KAFKA_BROKER` and `KAFKA_TOPIC` environment variables in your terminal or in the code:
   ```bash
   export KAFKA_BROKER=your_kafka_broker
   export KAFKA_TOPIC=your_kafka_topic
  

Usage
Run the assistant with:
```bash
python intrusion_detection_system.py
Type your queries in the terminal. Type exit to end the session.
```

Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

License
Distributed under the MIT License. See LICENSE for details.

Contact
Rachna Pandya - LinkedIn | Email
GitHub: rachnapandya
