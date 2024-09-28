from kafka import KafkaProducer
import time

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Change to your Kafka broker address if needed
    value_serializer=lambda v: v.encode('utf-8')  # Serialize strings to bytes
)

# Send messages to Kafka topic
def send_message(producer, topic, key, value):
    producer.send(topic, key=key.encode('utf-8'), value=value)
    print(f"Sent message to {topic}: {key} -> {value}")

# Example usage
if __name__ == "__main__":
    topic = 'car_details'

    # Send some test messages as strings
    for i in range(5):
        key = f'test-key-{i}'
        value = f'Test message {i} at {time.time()}'
        send_message(producer, topic, key, value)
        time.sleep(1)  # Pause 1 second between messages

    # Ensure all messages are sent before closing
    producer.flush()
    producer.close()
