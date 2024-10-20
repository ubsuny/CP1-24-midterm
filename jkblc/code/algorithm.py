"""Algorithms"""

import math
from datetime import datetime

def convert_to_unix_time(date_string, date_format="%Y-%m-%d %H:%M:%S"):
    """
    Convert a date string with a given format to Unix time.
    """
    dt = datetime.strptime(date_string, date_format)
    unix_time = int(dt.timestamp())
    return unix_time

def read_metafile_and_extract_unix(file_path):
    """
    Read a metafile, extract date and time, and convert it to Unix time.
    Assumes each line contains a timestamp in the format: YYYY-MM-DD HH:MM:SS.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            date_string = line.strip()
            yield convert_to_unix_time(date_string)

def direction_from_acceleration(ax, ay, az):
    """
    Calculate the direction of motion in 3D space from acceleration data.
    Returns the polar and azimuthal angles (in degrees).
    """
    # Calculate the magnitude of the vector
    magnitude = math.sqrt(ax**2 + ay**2 + az**2)

    # Avoid division by zero
    if magnitude == 0:
        raise ValueError("Zero acceleration vector, cannot determine direction.")

    # Calculate the polar angle θ (angle from z-axis)
    theta = math.acos(az / magnitude)

    # Calculate the azimuthal angle φ (angle in x-y plane)
    phi = math.atan2(ay, ax)

    # Convert radians to degrees
    theta_deg = math.degrees(theta)
    phi_deg = math.degrees(phi)

    return theta_deg, phi_deg

def haversine(coord1, coord2):
    """
    Calculate the great-circle distance between two points on Earth 
    given their latitude and longitude in decimal degrees.
    """
    # Radius of the Earth in meters
    radius = 6371000

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in meters
    return radius * c

def feet_to_meters(feet):
    """Convert feet to meters."""
    return feet * 0.3048

def yards_to_meters(yards):
    """Convert yards to meters."""
    return yards * 0.9144
