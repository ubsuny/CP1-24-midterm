"""
This module provides functions to extract date and time from a markdown
file and convert it into Unix time.
"""

import re
from datetime import datetime
import time

def extract_date_time(markdown_file):
    """
    Extracts the date and time from the specified markdown file and converts
    it into Unix time.

    markdown_file: The name of the markdown file to read.

    Returns: The Unix time representation of the extracted date and time.

    Outputs: ValueError: If the date or time is not found in the markdown file.
    """

    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use regex to find date and time
    date_match = re.search(r'-\s*(\d{1,2}/\d{1,2}/\d{4})', content)
    time_match = re.search(r'-\s*(\d{1,2}:\d{2}\s*[APM]{2})', content)

    if date_match and time_match:
        date_str = date_match.group(1)
        time_str = time_match.group(1)

        # Combine date and time strings
        datetime_str = f"{date_str} {time_str}"

        # Convert to Unix time
        dt = datetime.strptime(datetime_str, '%m/%d/%Y %I:%M %p')
        unix_time = int(time.mktime(dt.timetuple()))

        return unix_time
    else:
        raise ValueError("Date or time not found in the markdown file.")

if __name__ == "__main__":
    markdown_file = input("Enter the markdown file name (with .md extension): ")
    try:
        unix_time = extract_date_time(markdown_file)
        print(f"Unix time: {unix_time}")
    except ValueError as e:  # Catch specific exception
        print(e)
    except Exception as e:  # Keep a broad exception catch for other errors
        print(e)

