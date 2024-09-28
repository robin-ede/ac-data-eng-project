from typing import Dict, List

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def transform(messages: List[Dict], *args, **kwargs) -> List[Dict]:
    """
    Transformer function to convert car telemetry data.

    Args:
        messages: List of messages in the stream.

    Returns:
        List of transformed messages.
    """
    transformed_data = []

    for i, message in enumerate(messages):
        print(f"Processing message {i}: {message}")

        # Create a flat dictionary for each transformed message
        transformed_message = {
            'event_time': message.get('event_time'),
            'car_id': message.get('car_id'),
            'speed_kmh': message.get('speed_kmh'),
            'rpm': message.get('rpm'),
            'fuel_level': message.get('fuel_level'),
            'gear': message.get('gear'),
            'driver': message.get('driver'),
            # Derived fields
            'speed_mph': round(message.get('speed_kmh', 0) * 0.621371, 2) if message.get('speed_kmh') is not None else None,
            'timestamp': datetime.utcnow().isoformat(),
        }

        # Calculate engine load if gear > 0, otherwise set to 0.0
        rpm = message.get('rpm', 0)
        gear = message.get('gear', 0)
        if gear > 0:
            transformed_message['engine_load'] = round((rpm / (gear * 1000)) * 100, 2)
        else:
            transformed_message['engine_load'] = 0.0

        print(f"Transformed message {i}: {transformed_message}")

        # Append transformed message to the list
        transformed_data.append(transformed_message)

    return transformed_data
