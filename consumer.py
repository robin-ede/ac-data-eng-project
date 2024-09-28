from kafka import KafkaConsumer

consumer = KafkaConsumer('car_details', bootstrap_servers='localhost:9092')

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
