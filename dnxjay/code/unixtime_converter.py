"""This module provides functions to convert date and time strings into Unix timestamps.
It supports multiple date and time formats and allows optional Unix time adjustments.

Unix time, also known as POSIX time or Epoch time, represents the number of seconds
that have elapsed since January 1, 1970 (UTC). This module simplifies converting
various date and time formats into Unix timestamps for consistency and further analysis.
"""

from datetime import datetime

def to_unix_time(date_str, time_str, date_format="%B %d, %Y", time_format="%I:%M %p", adjustment_seconds=0):
    """Convert date and time strings to a Unix timestamp.
    
    Args:
        date_str (str): The date string (e.g., "October 24, 2024").
        time_str (str): The time string (e.g., "11:09 AM").
        date_format (str): The format of the date string, defaulting to "%B %d, %Y".
        time_format (str): The format of the time string, defaulting to "%I:%M %p".
        adjustment_seconds (int): Optional adjustment to the Unix time (in seconds),
                                  positive or negative.

    Returns:
        int: The Unix timestamp representing the provided date and time,
             with any optional adjustment applied.

    Raises:
        ValueError: If the provided date or time string does not match the specified formats.
    """
    datetime_str = f"{date_str} {time_str}"
    full_format = f"{date_format} {time_format}"

    try:
        dt_obj = datetime.strptime(datetime_str, full_format)
    except ValueError:
        raise ValueError(f"Error: Provided date or time does not match the format: '{full_format}'")

    unix_time = int(dt_obj.timestamp()) + adjustment_seconds
    return unix_time

def from_unix_time(unix_timestamp, output_format="%B %d, %Y %I:%M %p"):
    """Convert a Unix timestamp to a formatted date and time string.
    
    Args:
        unix_timestamp (int): The Unix timestamp to convert.
        output_format (str): The format string for the output.

    Returns:
        str: The formatted date and time string representing the Unix timestamp.
    """
    dt_obj = datetime.fromtimestamp(unix_timestamp)
    return dt_obj.strftime(output_format)

def validate_datetime_format(date_str, time_str, date_format="%B %d, %Y", time_format="%I:%M %p"):
    """Validate if the date and time strings match the specified formats.
    
    Args:
        date_str (str): The date string (e.g., "October 24, 2024").
        time_str (str): The time string (e.g., "11:09 AM").
        date_format (str): Expected format for the date string.
        time_format (str): Expected format for the time string.

    Returns:
        bool: True if both date and time match the formats, False otherwise.
    """
    datetime_str = f"{date_str} {time_str}"
    full_format = f"{date_format} {time_format}"

    try:
        datetime.strptime(datetime_str, full_format)
        return True
    except ValueError:
        return False
