from typing import Dict, List
from datetime import datetime, timedelta

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

def milliseconds_to_timestamp(ms: int) -> str:
    """
    Convert milliseconds to a timestamp in the format HH:MM:SS.sss

    Args:
        ms: Milliseconds to convert

    Returns:
        A string representing the time in HH:MM:SS.sss format
    """
    if ms <= 0:
        return "00:00:00.000"
    td = timedelta(milliseconds=ms)
    return str(td)

@transformer
def transform(messages: List[Dict], *args, **kwargs) -> List[Dict]:
    """
    Transformer function to convert car telemetry data.

    Args:
        messages: List of messages in the stream.

    Returns:
        List of transformed messages.
    """
    transformed_messages = []

    for i, message in enumerate(messages):
        # Cleaning the strings with null characters
        car_id = message.get('car_id', '').replace('\u0000', '').strip()
        player_name = message.get('player_name', '').replace('\u0000', '').strip()
        track_status = message.get('track_status', '').replace('\u0000', '').strip()

        # Create a flat dictionary for each transformed message
        transformed_message = {
            'timestamp': message.get('timestamp'),
            'car_id': car_id,
            'player_name': player_name,
            'pos': message.get('position'),
            'completed_lap': message.get('completed_lap'),
            'current_lap_time': milliseconds_to_timestamp(message.get('current_lap_time', 0)),
            'last_lap_time': milliseconds_to_timestamp(message.get('last_lap_time', 0)),
            'best_lap_time': milliseconds_to_timestamp(message.get('best_lap_time', 0)),
            'estimated_lap_time': milliseconds_to_timestamp(message.get('estimated_lap_time', 0)),
            'current_sector': message.get('current_sector'),
            'session_time': milliseconds_to_timestamp(message.get('session_time_left', 0) * -1),
            'speed_kmh': message.get('speed_kmh'),
            'rpm': message.get('rpm'),
            'gear': message.get('gear'),
            'fuel_level': message.get('fuel_level'),
            'fuel_per_lap': message.get('fuel_per_lap'),
            'tyre_pressure_front_left': message.get('tyre_pressure', {}).get('front_left'),
            'tyre_pressure_front_right': message.get('tyre_pressure', {}).get('front_right'),
            'tyre_pressure_rear_left': message.get('tyre_pressure', {}).get('rear_left'),
            'tyre_pressure_rear_right': message.get('tyre_pressure', {}).get('rear_right'),
            'tyre_core_temp_front_left': message.get('tyre_core_temp', {}).get('front_left'),
            'tyre_core_temp_front_right': message.get('tyre_core_temp', {}).get('front_right'),
            'tyre_core_temp_rear_left': message.get('tyre_core_temp', {}).get('rear_left'),
            'tyre_core_temp_rear_right': message.get('tyre_core_temp', {}).get('rear_right'),
            'brake_temp_front_left': message.get('brake_temp', {}).get('front_left'),
            'brake_temp_front_right': message.get('brake_temp', {}).get('front_right'),
            'brake_temp_rear_left': message.get('brake_temp', {}).get('rear_left'),
            'brake_temp_rear_right': message.get('brake_temp', {}).get('rear_right'),
            'g_force_x': message.get('g_force', {}).get('x'),
            'g_force_y': message.get('g_force', {}).get('y'),
            'g_force_z': message.get('g_force', {}).get('z'),
            'rain_intensity': message.get('rain_intensity'),
            'rain_intensity_in_10min': message.get('rain_intensity_in_10min'),
            'rain_intensity_in_30min': message.get('rain_intensity_in_30min'),
            'track_grip_status': message.get('track_grip_status'),
            'track_status': track_status,
            'car_damage_front': message.get('car_damage', {}).get('front'),
            'car_damage_rear': message.get('car_damage', {}).get('rear'),
            'car_damage_left': message.get('car_damage', {}).get('left'),
            'car_damage_right': message.get('car_damage', {}).get('right'),
            'car_damage_center': message.get('car_damage', {}).get('center'),
            'gap_ahead': milliseconds_to_timestamp(message.get('gaps', {}).get('gap_ahead', 0)),
            'gap_behind': milliseconds_to_timestamp(message.get('gaps', {}).get('gap_behind', 0)),
            'flag_status': message.get('flag_status'),
            'penalty': message.get('penalty'),
            'pit_limiter_on': message.get('pit_limiter_on'),
            'wind_speed': message.get('wind_speed'),
            'wind_direction': message.get('wind_direction'),
            'session_type': message.get('session_type'),
            'tc_level': message.get('tc_level'),
            'abs_level': message.get('abs_level'),
            'is_in_pit_lane': message.get('is_in_pit_lane'),
            'fuel_estimated_laps': message.get('fuel_estimated_laps'),
            'current_tyre_set': message.get('current_tyre_set'),
            'delta_lap_time': milliseconds_to_timestamp(message.get('delta_lap_time', 0)),
            'exhaust_temp': message.get('exhaust_temp')
        }

        # Append transformed message to the list of transformed messages
        transformed_messages.append(transformed_message)

    return transformed_messages


