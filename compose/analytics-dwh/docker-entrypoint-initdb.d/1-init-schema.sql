-- Create a new database named 'analytics'
CREATE DATABASE IF NOT EXISTS analytics;

-- Use the 'analytics' database
USE analytics;

-- Create a table for storing Kafka events (e.g., car telemetry data)
CREATE TABLE car_telemetry (
    event_time DateTime,
    car_id String,
    speed_kmh Float32,
    rpm Int32,
    fuel_level Float32,
    gear Int8,
    driver String
) ENGINE = MergeTree()
ORDER BY (event_time, car_id);