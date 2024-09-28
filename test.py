from pyaccsharedmemory import accSharedMemory
import json
from kafka import KafkaProducer
import time

# Initialize the ACC shared memory reader
asm = accSharedMemory()
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "car_details"

def extract_car_details():
    sm = asm.read_shared_memory()
    if sm is not None:
        car_data = {
            "speed_kmh": sm.Physics.speed_kmh,
            "gear": sm.Physics.gear,
            "rpm": sm.Physics.rpm,
            "fuel": sm.Physics.fuel,
            "tyre_pressure": {
                "front_left": sm.Physics.wheel_pressure.front_left,
                "front_right": sm.Physics.wheel_pressure.front_right,
                "rear_left": sm.Physics.wheel_pressure.rear_left,
                "rear_right": sm.Physics.wheel_pressure.rear_right,
            },
            "car_model": sm.Static.car_model,
            "track": sm.Static.track,
            "player_name": sm.Static.player_name
        }
        
        return car_data
    return None

try:
    while True:
        car_details = extract_car_details()
        if car_details:
            # Send car details to Kafka
            producer.send(topic, car_details)
            print(f"Sent data to Kafka: {car_details}")
        
        # Wait a moment before reading again
        time.sleep(1)

except KeyboardInterrupt:
    asm.close()
    producer.close()
    print("Shutting down...")

