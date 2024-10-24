"""
This module contains utility functions that do not belong as first order
members of the Trip class.

List out classes and functions:...

"""
import pandas as pd
import numpy as np
from datetime import datetime

class CSVImportError(Exception):
    """
    Custom exception raised when a CSV file cannot be imported.
    Provides an error message with details about the failure.
    """
    def __init__(self, message):
        super().__init__(message)

def convert_to_meters(value, unit):
    """
    Converts a given value from a specified unit to meters. This function
    uses exact quantities for conversion factors exclusively.

    Args:
        value (number): The numerical value to be converted.
        unit (str): The unit of the value to convert from. Supported units
        include:
                    'km' (kilometers), 'cm' (centimeters), 'mm' (millimeters),
                    'inch' (inches), 'ft' (feet), 'yd' (yards), 'mile' (miles).

    Returns:
        Number: The equivalent value in meters (a float).

    Raises:
        ValueError: If the specified unit is not supported.
    """
    # Let's store the unit coverstion factors neatly within in a dict.
    conversion_factors = {
        'km': 1000.0,          # Kilometers to meters (exact quantity)
        'cm': 0.0100,          # Centimeters to meters (exact quantity)
        'mm': 0.0010,         # Millimeters to meters (exact quantity)
        'inch': 0.0254,      # Inches to meters (exact quantity)
        'in': 0.0254,      # Inches to meters (exact quantity)
        'ft': 0.3048,        # Feet to meters (exact quantity)
        'feert': 0.3048,        # Feet to meters (exact quantity)
        'yd': 0.9144,        # Yards to meters (exact quantity)
        'yard': 0.9144,        # Yards to meters (exact quantity)
        'mile': 1609.344,      # Miles to meters (exact quantity)
        'ml': 1609.344      # Miles to meters (exact quantity)
    }

    # Convert the value using the conversion factor for the unit
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        raise ValueError(f"Unknown unit: {unit}")

def import_csv(csv_path):
    """
    Imports data from a CSV file (that uses commas, not semicolons) into a
     pandas DataFrame. It is then returned to the caller.

    Args:
        csv_path (str): The path to the CSV file.

    Returns:
        DataFrame: The data from the CSV file as a pandas DataFrame.
    """
    # Attempt to read in the csv, or throw the proper exception
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_path)
        # Return it to the calling function
        return df

    # If the the file can't be found
    # Throw the exception, print the error, and return None
    except FileNotFoundError as e:
        print(f"Error: The file '{csv_path}' was not found.")
        print(f"Details: {str(e)}")
        return None
    # If the file is empty
    # Throw an exception, print the error, and return None
    except pd.errors.EmptyDataError as e:
        print(f"Error: The file '{csv_path}' is empty.")
        print(f"Details: {str(e)}")
        return None
    # If the file is malformed and cannot be parsed
    # Throw an exception, print the error, and return None
    except pd.errors.ParserError as e:
        print(f"Error: The file '{csv_path}' could not be parsed.")
        print(f"Details: {str(e)}")
        return None

def timecode_to_unix(time_str):
    """
    Converts a time string in the ddefault format 'YYYY-MM-DD HH:MM:SS.sss
    UTC±HH:MM' to Unix time.

    Args:
        time_str (str): A string representing the time with timezone.

    Returns:
        int: Unix timestamp corresponding to the given time.
    """
    # Parse the string into a datetime object with timezone info
    dt_with_tz = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f %Z%z')

    # Convert to Unix timestamp
    unix_time = int(dt_with_tz.timestamp())

    return unix_time

def haversine_with_altitude(lat1, lon1, lat2, lon2, alt1, alt2):
    """
    Calculate the 3D great-circle distance between two points on the Earth's
    surface, including altitude differences.

    The output distance is in meters.

    Args:
        lat1, lon1, alt1: Latitude, Longitude, and Altitude of point 1.
        lat2, lon2, alt2: Latitude, Longitude, and Altitude of point 2.

    Returns:
        distance (float): The 3D distance between the two points in meters.
    """
    R = 6371.0  # Radius of Earth in kilometers

    # Convert degrees to radians
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    # Differences in latitudes, longitudes, and altitudes
    dlat = lat2 - lat1  # Lat dif in radians
    dlon = lon2 - lon1  # Long dif in radians
    dalt = alt2 - alt1  # Altitude difference in meters

    # Haversine formula for the distance over the Earth's surface (in kilometers)
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    surface_distance_km = R * c  # Distance in kilometers

    # Convert surface distance to meters
    surface_distance_m = surface_distance_km * 1000  # Convert to meters

    # 3D distance, considering altitude
    distance_3d = np.sqrt(surface_distance_m**2 + dalt**2)

    return distance_3d
