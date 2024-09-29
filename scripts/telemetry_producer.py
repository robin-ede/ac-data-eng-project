from pyaccsharedmemory import accSharedMemory
import json
from kafka import KafkaProducer
import time
from datetime import datetime

# Initialize the ACC shared memory reader
asm = accSharedMemory()
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "car_details"

try:
    # Continuously read telemetry data and send to Kafka
    while True:
        # Read the shared memory
        sm = asm.read_shared_memory()

        # If data is available
        if sm is not None:
            # Create a dictionary to store telemetry information
            telemetry_data = {
                'timestamp': datetime.now().isoformat(),  # Current timestamp
                'car_id': sm.Static.car_model,  # Car model
                'player_name': sm.Static.player_name,  # Player name
                'position': sm.Graphics.position,  # Current player position
                'completed_lap': sm.Graphics.completed_lap,  # Number of completed laps
                'current_lap_time': sm.Graphics.current_time,  # Current lap time in milliseconds
                'last_lap_time': sm.Graphics.last_time,  # Last lap time in milliseconds
                'best_lap_time': sm.Graphics.best_time,  # Best lap time in milliseconds
                'estimated_lap_time': sm.Graphics.estimated_lap_time,  # Estimated lap time in milliseconds
                'current_sector': sm.Graphics.current_sector_index,  # Current track sector
                'session_time_left': sm.Graphics.session_time_left,  # Session time left
                'speed_kmh': sm.Physics.speed_kmh,  # Car speed in km/h
                'rpm': sm.Physics.rpm,  # Engine RPM
                'gear': sm.Physics.gear,  # Current gear
                'fuel_level': sm.Physics.fuel,  # Amount of fuel remaining in liters
                'fuel_per_lap': sm.Graphics.fuel_per_lap,  # Average fuel consumed per lap
                'tyre_pressure': {
                    'front_left': sm.Physics.wheel_pressure.front_left,
                    'front_right': sm.Physics.wheel_pressure.front_right,
                    'rear_left': sm.Physics.wheel_pressure.rear_left,
                    'rear_right': sm.Physics.wheel_pressure.rear_right,
                },  # Tyre pressures
                'tyre_core_temp': {
                    'front_left': sm.Physics.tyre_core_temp.front_left,
                    'front_right': sm.Physics.tyre_core_temp.front_right,
                    'rear_left': sm.Physics.tyre_core_temp.rear_left,
                    'rear_right': sm.Physics.tyre_core_temp.rear_right,
                },  # Tyre core temperatures
                'brake_temp': {
                    'front_left': sm.Physics.brake_temp.front_left,
                    'front_right': sm.Physics.brake_temp.front_right,
                    'rear_left': sm.Physics.brake_temp.rear_left,
                    'rear_right': sm.Physics.brake_temp.rear_right,
                },  # Brake disc temperatures
                'g_force': {
                    'x': sm.Physics.g_force.x,
                    'y': sm.Physics.g_force.y,
                    'z': sm.Physics.g_force.z,
                },  # G-force values
                'rain_intensity': sm.Graphics.rain_intensity.name,  # Rain intensity
                'track_grip_status': sm.Graphics.track_grip_status.name,  # Track grip status
                'track_status': sm.Graphics.track_status,  # Track status
                'car_damage': {
                    'front': sm.Physics.car_damage.front,
                    'rear': sm.Physics.car_damage.rear,
                    'left': sm.Physics.car_damage.left,
                    'right': sm.Physics.car_damage.right,
                    'center': sm.Physics.car_damage.center
                },  # Car damage details
                'gaps': {
                    'gap_ahead': sm.Graphics.gap_ahead,  # Gap to the car ahead in milliseconds
                    'gap_behind': sm.Graphics.gap_behind  # Gap to the car behind in milliseconds
                },
                'flag_status': str(sm.Graphics.flag),  # Current flag status
                'penalty': str(sm.Graphics.penalty),  # Current penalty status
                'pit_limiter_on': sm.Physics.pit_limiter_on,  # Pit limiter status
                'wind_speed': sm.Graphics.wind_speed,  # Wind speed
                'wind_direction': sm.Graphics.wind_direction,  # Wind direction
                'session_type': sm.Graphics.session_type.name,  # Session type
                'tc_level': sm.Graphics.tc_level,  # Traction control level
                'abs_level': sm.Graphics.abs_level,  # ABS level
                'is_in_pit_lane': sm.Graphics.is_in_pit_lane,  # Whether the car is in the pit lane
                'fuel_estimated_laps': sm.Graphics.fuel_estimated_laps,  # Estimated laps possible with current fuel
                'current_tyre_set': sm.Graphics.current_tyre_set,  # Current tyre set
                'delta_lap_time': sm.Graphics.delta_lap_time,  # Delta lap time in milliseconds
                'exhaust_temp': sm.Graphics.exhaust_temp,  # Exhaust temperature
            }

            # Produce message to Kafka topic 'car_details'
            producer.send(topic, telemetry_data)

            print(f"Sent message: {telemetry_data}")

        # Wait before polling for new data (adjust this based on your preference)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopping producer...")

finally:
    # Clean up
    asm.close()
    producer.flush()
