# test_gps_distance.py

from gps_distance import haversine, cumulative_distance, total_distance
import pytest

def test_haversine():
    # Check distance between points in different units
    assert haversine(0, 0, 0, 1) == pytest.approx(111194.93, rel=1e-4)
    assert haversine(0, 0, 0, 1, unit="kilometers") == pytest.approx(111.1949, rel=1e-4)
    assert haversine(0, 0, 0, 1, unit="miles") == pytest.approx(69.09, rel=1e-4)

    # Extreme latitudes/longitudes
    assert haversine(90, 0, -90, 0) == pytest.approx(20015114.35, rel=1e-4)  # Pole to pole
    assert haversine(0, 180, 0, -180) == pytest.approx(0.0, abs=1e-8)  # Near-zero tolerance

    # Test invalid units
    with pytest.raises(ValueError):
        haversine(0, 0, 1, 0, unit="feet")

def test_cumulative_distance():
    # Test cumulative distances with multiple points
    latitudes = [0, 1, 2, 3]
    longitudes = [0, 1, 2, 3]
    distances = cumulative_distance(latitudes, longitudes, unit="meters")
    assert len(distances) == len(latitudes) - 1
    assert distances[-1] == pytest.approx(471652.37, rel=1e-4)

    # Non-sequential points
    latitudes = [0, 0, 90]
    longitudes = [0, 90, 0]
    distances = cumulative_distance(latitudes, longitudes, unit="kilometers")
    assert distances[-1] == pytest.approx(20015.09, rel=1e-4)  # Half Earth's circumference

def test_total_distance():
    # Straight line path distance test
    latitudes = [0, 1, 2, 3]
    longitudes = [0, 1, 2, 3]
    assert total_distance(latitudes, longitudes, unit="meters") == pytest.approx(471652.37, rel=1e-4)

    # Check 0 distance for single point
    assert total_distance([0], [0]) == 0

    # Test with points along the equator
    latitudes = [0, 0, 0]
    longitudes = [0, 90, 180]
    assert total_distance(latitudes, longitudes, unit="kilometers") == pytest.approx(20015.09, rel=1e-4)  # Half Earth's circumference
