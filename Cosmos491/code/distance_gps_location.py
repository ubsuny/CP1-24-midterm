import numpy as np
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on Earth using the Haversine formula.

    Parameters:
    lat1, lon1: Latitude and Longitude of point 1 (in decimal degrees).
    lat2, lon2: Latitude and Longitude of point 2 (in decimal degrees).

    Returns:
    float: Distance between the two points in meters.
    """
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    # Radius of the Earth in meters
    R = 6378137
    return R * c  # Distance in meters
