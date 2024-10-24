import pytest
import numpy as np
from code.distance_gps_location.py import haversine 

def test_haversine():
    # Test with known distance between two points (Paris and London)
    lat1, lon1 = 48.8566, 2.3522  # Paris
    lat2, lon2 = 51.5074, -0.1278  # London
    expected_distance = 343_556  # Approx. 343.556 km in meters
    distance = haversine(lat1, lon1, lat2, lon2)
    assert np.isclose(distance, expected_distance, rtol=1e-3)

    # Test with same point (distance should be 0)
    assert haversine(lat1, lon1, lat1, lon1) == 0

    # Test with edge case (coordinates at poles)
    assert haversine(90, 0, -90, 0) == pytest.approx(2 * 6378137 * np.pi / 2)  # Half Earth's circumference
