"""This module provides functions to convert date and time strings into Unix timestamps.
It supports multiple date and time formats and allows optional Unix time adjustments.

Unix time, also known as POSIX time or Epoch time, represents the number of seconds
that have elapsed since January 1, 1970 (UTC). This module simplifies converting
various date and time formats into Unix timestamps for consistency and further analysis.
"""

from datetime import datetime

def to_unix_time(date_str, time_str, date_format="%B %dth, %Y", time_format="%I:%M %p", adjustment_seconds=0):
    """Convert date and time strings to a Unix timestamp.
    
    This function accepts a date and time string, along with optional format specifications
    and an adjustment in seconds, to convert the date and time into a Unix timestamp.

    Args:
        date_str (str): The date string (e.g., "October 24th, 2024").
        time_str (str): The time string (e.g., "11:09 AM").
        date_format (str): The format of the date string, defaulting to "%B %dth, %Y".
                           For example, use "%B %d, %Y" if your date is like "October 24, 2024".
        time_format (str): The format of the time string, defaulting to "%I:%M %p".
                           For example, use "%H:%M" for 24-hour time format.
        adjustment_seconds (int): Optional adjustment to the Unix time (in seconds),
                                  positive or negative.

    Returns:
        int: The Unix timestamp representing the provided date and time,
             with any optional adjustment applied.

    Raises:
        ValueError: If the provided date or time string does not match the specified formats.
    """
    # Combine date and time into a single string
    datetime_str = f"{date_str} {time_str}"
    full_format = f"{date_format} {time_format}"

    try:
        # Parse the combined datetime string into a datetime object
        dt_obj = datetime.strptime(datetime_str, full_format)
    except ValueError:
        raise ValueError(f"Error: Provided date or time does not match the format: '{full_format}'")

    # Convert datetime to Unix timestamp
    unix_time = int(dt_obj.timestamp())

    # Apply any optional adjustment
    if adjustment_seconds != 0:
        unix_time += adjustment_seconds

    return unix_time

def from_unix_time(unix_timestamp, output_format="%B %d, %Y %I:%M %p"):
    """Convert a Unix timestamp to a formatted date and time string.
    
    This function provides a readable date and time string based on the specified output format.

    Args:
        unix_timestamp (int): The Unix timestamp to convert.
        output_format (str): The format string for the output (default is "%B %d, %Y %I:%M %p").

    Returns:
        str: The formatted date and time string representing the Unix timestamp.
    """
    # Convert Unix timestamp to datetime object
    dt_obj = datetime.fromtimestamp(unix_timestamp)

    # Format the datetime object according to the specified output format
    formatted_datetime = dt_obj.strftime(output_format)

    return formatted_datetime

def validate_datetime_format(date_str, time_str, date_format="%B %dth, %Y", time_format="%I:%M %p"):
    """Validate if the date and time strings match the specified formats.
    
    This function checks if a date and time string are compatible with the given formats.
    It helps catch format errors before attempting Unix conversion.

    Args:
        date_str (str): The date string (e.g., "October 24th, 2024").
        time_str (str): The time string (e.g., "11:09 AM").
        date_format (str): Expected format for the date string.
        time_format (str): Expected format for the time string.

    Returns:
        bool: True if both date and time match the formats, False otherwise.
    """
    datetime_str = f"{date_str} {time_str}"
    full_format = f"{date_format} {time_format}"

    try:
        # Try to parse the string according to the format
        datetime.strptime(datetime_str, full_format)
        return True
    except ValueError:
        return False

# Example usage of the functions
if __name__ == "__main__":
    date_input = input("Enter the date (e.g., 'October 24th, 2024'): ")
    time_input = input("Enter the time (e.g., '11:09 AM'): ")
    
    # Convert to Unix time with an optional adjustment
    try:
        unix_timestamp = to_unix_time(date_input, time_input, adjustment_seconds=0)
        print(f"Unix Timestamp: {unix_timestamp}")

        # Convert back to readable date format
        print("Formatted Date and Time:", from_unix_time(unix_timestamp))
    except ValueError as e:
        print(f"Error: {e}")
