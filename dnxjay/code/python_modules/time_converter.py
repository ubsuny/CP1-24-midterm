# time_converter.py
from datetime import datetime

def to_unix_time(date_str, time_str):
    """Convert date and time strings to Unix time.
    
    Args:
        date_str (str): Date in format "Month day, Year" (e.g., "October 24th, 2024").
        time_str (str): Time in format "HH:MM AM/PM" (e.g., "11:09 AM").
        
    Returns:
        int: Unix timestamp (seconds since January 1, 1970).
    """
    datetime_str = f"{date_str} {time_str}"
    dt_obj = datetime.strptime(datetime_str, "%B %dth, %Y %I:%M %p")
    return int(dt_obj.timestamp())
