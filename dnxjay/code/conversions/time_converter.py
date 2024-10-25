from datetime import datetime

def to_unix_time(date_str, time_str):
    """Convert date and time strings to Unix time."""
    datetime_str = f"{date_str} {time_str}"
    dt_obj = datetime.strptime(datetime_str, "%B %dth, %Y %I:%M %p")
    return int(dt_obj.timestamp())
