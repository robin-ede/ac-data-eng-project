CREATE TABLE car_telemetry (
    _timestamp TIMESTAMP,  -- Represents the actual event timestamp
    car_id TEXT,
    player_name TEXT,
    pos INTEGER,
    completed_lap INTEGER,
    current_lap_time INTERVAL,  -- Represents the current lap time as an interval
    last_lap_time INTERVAL,     -- Represents the last lap time as an interval
    best_lap_time INTERVAL,     -- Represents the best lap time as an interval
    estimated_lap_time INTERVAL, -- Represents the estimated lap time as an interval
    current_sector INTEGER,
    session_time INTERVAL,
    speed_kmh REAL,
    rpm INTEGER,
    gear INTEGER,
    fuel_level REAL,
    fuel_per_lap REAL,
    tyre_pressure_front_left REAL,
    tyre_pressure_front_right REAL,
    tyre_pressure_rear_left REAL,
    tyre_pressure_rear_right REAL,
    tyre_core_temp_front_left REAL,
    tyre_core_temp_front_right REAL,
    tyre_core_temp_rear_left REAL,
    tyre_core_temp_rear_right REAL,
    brake_temp_front_left REAL,
    brake_temp_front_right REAL,
    brake_temp_rear_left REAL,
    brake_temp_rear_right REAL,
    g_force_x REAL,
    g_force_y REAL,
    g_force_z REAL,
    rain_intensity TEXT,
    rain_intensity_in_10min TEXT,
    rain_intensity_in_30min TEXT,
    track_grip_status TEXT,
    track_status TEXT,
    car_damage_front REAL,
    car_damage_rear REAL,
    car_damage_left REAL,
    car_damage_right REAL,
    car_damage_center REAL,
    gap_ahead INTERVAL,  -- Represents the gap ahead in milliseconds or seconds
    gap_behind INTERVAL, -- Represents the gap behind in milliseconds or seconds
    flag_status TEXT,
    penalty TEXT,
    pit_limiter_on BOOLEAN,
    wind_speed REAL,
    wind_direction REAL,
    session_type TEXT,
    tc_level INTEGER,
    abs_level INTEGER,
    is_in_pit_lane BOOLEAN,
    fuel_estimated_laps REAL,
    current_tyre_set INTEGER,
    delta_lap_time INTERVAL,  -- Represents the delta lap time as an interval
    exhaust_temp REAL
);
