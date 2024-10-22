import time
from datetime import datetime

def read_text_metafile(filename):
    """
    Read metadata from a text file and return it as a dictionary.

    Parameters:
    filename -- Path to the metafile (e.g., 'metadata.txt').

    Returns:
    A dictionary containing the metadata.
    """
    metadata = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(": ", 1)
            metadata[key] = value
    return metadata


def convert_to_unix_time(date_str, time_str=None):
    """
    Convert a date (and optional time) string to Unix time.
    
    Parameters:
    date_str -- A string representing the date (e.g., '2024-10-21').
    time_str -- A string representing the time (optional, e.g., '14:30:00').
                If no time is provided, '00:00:00' is assumed.

    Returns:
    Unix time (seconds since January 1, 1970).
    """
    # Combine date and time strings if time is provided, else use '00:00:00'
    datetime_str = f"{date_str} {time_str}" if time_str else f"{date_str} 00:00:00"

    # Parse the datetime string into a datetime object
    dt_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

    # Convert the datetime object to Unix time (seconds since the epoch)
    unix_time = int(time.mktime(dt_obj.timetuple()))
    return unix_time


def get_unix_time_from_metafile(metafile):
    """
    Read the date and time from a metafile and convert it to Unix time.

    Parameters:
    metafile -- Path to the metafile (e.g., 'metadata.txt').

    Returns:
    Unix time (seconds since January 1, 1970) for the given date and time.
    """
    metadata = read_text_metafile(metafile)

    # Check if the required fields are in the metadata
    date = metadata.get('Date')
    time = metadata.get('Time')  # Optional, might be 'None' if not in the file

    if not date:
        raise ValueError("Date not found in metafile.")

    # Convert date and time to Unix time
    unix_time = convert_to_unix_time(date, time)
    return unix_time


# Example usage
if __name__ == "__main__":
    metafile = '/workspaces/CP1-24-midterm/Kylemasc917/data/Kylemascmetafile0111.txt'  # Path to the metafile

    # Read and convert date/time from metafile to Unix time
    unix_time = get_unix_time_from_metafile(metafile)
    print(f"Unix Time: {unix_time}")
