import pandas as pd
from datetime import datetime
from typing import Dict, List

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(messages: List[Dict], *args, **kwargs) -> pd.DataFrame:
    """
    Template code for a transformer block.

    Args:
        messages: List of messages in the stream.

    Returns:
        DataFrame of transformed messages.
    """
    print(f"Received {len(messages)} messages")
    transformed_messages = []

    # Transformation logic
    for i, message in enumerate(messages):
        print(f"Message {i}: {message}")
        transformed_message = message.copy()

        # Convert speed from km/h to mph
        speed_kmh = transformed_message.get('speed_kmh', 0)
        speed_mph = speed_kmh * 0.621371
        transformed_message['speed_mph'] = round(speed_mph, 2)

        # Add a timestamp for each message
        transformed_message['timestamp'] = datetime.utcnow().isoformat()

        # Calculate a hypothetical engine load based on RPM and gear
        rpm = transformed_message.get('rpm', 0)
        gear = transformed_message.get('gear', 0)
        if gear > 0:
            engine_load = (rpm / (gear * 1000)) * 100  # Hypothetical formula
            transformed_message['engine_load'] = round(engine_load, 2)
        else:
            transformed_message['engine_load'] = 0.0

        print(f"Transformed message: {transformed_message}")
        transformed_messages.append(transformed_message)

    # Convert transformed messages into a DataFrame
    df = pd.DataFrame(transformed_messages)

    # Print the DataFrame to verify
    print(f"Transformed DataFrame:\n{df}")

    return df