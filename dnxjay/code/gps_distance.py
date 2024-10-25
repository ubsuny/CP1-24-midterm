"""This module calculates the distance between GPS coordinates using the Haversine formula.
It supports calculating the distance between two points, cumulative distances across
a series of points, and allows the result to be returned in various units.

The Haversine formula takes into account the curvature of the Earth, providing an
accurate measure of the distance between two latitude/longitude coordinates.
"""

import numpy as np

# Earth radius constants in various units
EARTH_RADIUS_METERS = 6371e3
EARTH_RADIUS_KILOMETERS = 6371
EARTH_RADIUS_MILES = 3958.8

def haversine(lat1, lon1, lat2, lon2, unit="meters"):
    """Calculate the Haversine distance between two GPS coordinates.
    
    Args:
        lat1 (float): Latitude of the first point in decimal degrees.
        lon1 (float): Longitude of the first point in decimal degrees.
        lat2 (float): Latitude of the second point in decimal degrees.
        lon2 (float): Longitude of the second point in decimal degrees.
        unit (str): Unit of measurement for the output distance. Options are "meters",
                    "kilometers", and "miles". Defaults to "meters".

    Returns:
        float: The distance between the two points in the specified unit.

    Raises:
        ValueError: If the latitude or longitude values are out of range or if an invalid
                    unit is provided.
    """
    # Validate latitude and longitude ranges
    if not (-90 <= lat1 <= 90 and -90 <= lat2 <= 90):
        raise ValueError("Latitude values must be between -90 and 90 degrees.")
    if not (-180 <= lon1 <= 180 and -180 <= lon2 <= 180):
        raise ValueError("Longitude values must be between -180 and 180 degrees.")
    
    # Convert latitudes and longitudes from degrees to radians
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    
    # Haversine formula
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    # Select Earth radius based on the specified unit
    if unit == "meters":
        radius = EARTH_RADIUS_METERS
    elif unit == "kilometers":
        radius = EARTH_RADIUS_KILOMETERS
    elif unit == "miles":
        radius = EARTH_RADIUS_MILES
    else:
        raise ValueError("Invalid unit. Choose 'meters', 'kilometers', or 'miles'.")

    # Calculate distance
    return radius * c

def cumulative_distance(latitudes, longitudes, unit="meters"):
    """Calculate cumulative distance across a series of latitude and longitude points.
    
    Args:
        latitudes (list or np.ndarray): List or array of latitude points in decimal degrees.
        longitudes (list or np.ndarray): List or array of longitude points in decimal degrees.
        unit (str): Unit of measurement for the output distance. Options are "meters",
                    "kilometers", and "miles". Defaults to "meters".

    Returns:
        np.ndarray: Array of cumulative distances in the specified unit for each segment.

    Raises:
        ValueError: If the lengths of latitudes and longitudes do not match.
    """
    if len(latitudes) != len(longitudes):
        raise ValueError("Latitude and longitude arrays must have the same length.")

    # Calculate segment distances and accumulate them
    distances = [
        haversine(latitudes[i], longitudes[i], latitudes[i+1], longitudes[i+1], unit=unit)
        for i in range(len(latitudes) - 1)
    ]
    return np.cumsum(distances)

def total_distance(latitudes, longitudes, unit="meters"):
    """Calculate the total distance across a series of latitude and longitude points.
    
    Args:
        latitudes (list or np.ndarray): List or array of latitude points in decimal degrees.
        longitudes (list or np.ndarray): List or array of longitude points in decimal degrees.
        unit (str): Unit of measurement for the output distance. Options are "meters",
                    "kilometers", and "miles". Defaults to "meters".

    Returns:
        float: Total distance across all points in the specified unit.

    Raises:
        ValueError: If the lengths of latitudes and longitudes do not match.
    """
    cumulative_distances = cumulative_distance(latitudes, longitudes, unit=unit)
    return cumulative_distances[-1] if len(cumulative_distances) > 0 else 0

# Example usage
if __name__ == "__main__":
    # Example coordinates for testing
    latitudes = [42.3601, 42.3611, 42.3621]
    longitudes = [-71.0589, -71.0579, -71.0569]
    
    # Calculate the total distance in meters
    print("Total Distance (meters):", total_distance(latitudes, longitudes))
    
    # Calculate cumulative distances in kilometers
    print("Cumulative Distances (km):", cumulative_distance(latitudes, longitudes, unit="kilometers"))
