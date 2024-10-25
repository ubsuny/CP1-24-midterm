# unix_time_converter.py
import pandas as pd

def convert_to_unix(date_str, time_str):
    """
    Converts date and time to Unix timestamp.
    Example: convert_to_unix("2024-10-25", "14:30") -> 1733052600
    """
    dt = pd.to_datetime(f"{date_str} {time_str}")
    return int(dt.timestamp())