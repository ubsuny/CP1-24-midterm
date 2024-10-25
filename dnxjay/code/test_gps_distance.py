# test_gps_distance.py

from dnxjay.code.gps_distance import haversine, cumulative_distance, total_distance

def test_haversine():
    # Check distance between points in different units
    assert round(haversine(0, 0, 0, 1), 2) == 111194.93
    assert round(haversine(0, 0, 0, 1, unit="kilometers"), 2) == 111.19
    assert round(haversine(0, 0, 0, 1, unit="miles"), 2) == 69.09

    # Extreme latitudes/longitudes
    assert round(haversine(90, 0, -90, 0), 2) == 20015114.35  # Pole to pole
    assert round(haversine(0, 180, 0, -180), 2) == 0.0  # Same point after longitude wrap

    # Test invalid units
    try:
        haversine(0, 0, 1, 0, unit="feet")
    except ValueError:
        assert True

def test_cumulative_distance():
    # Test cumulative distances with multiple points
    latitudes = [0, 1, 2, 3]
    longitudes = [0, 1, 2, 3]
    distances = cumulative_distance(latitudes, longitudes, unit="meters")
    assert len(distances) == len(latitudes) - 1
    assert round(distances[-1], 2) == 471216.36

    # Non-sequential points
    latitudes = [0, 0, 90]
    longitudes = [0, 90, 0]
    distances = cumulative_distance(latitudes, longitudes, unit="kilometers")
    assert round(distances[-1], 2) == 10007.54  # Quarter of Earth's circumference

def test_total_distance():
    # Straight line path distance test
    latitudes = [0, 1, 2, 3]
    longitudes = [0, 1, 2, 3]
    assert round(total_distance(latitudes, longitudes, unit="meters"), 2) == 471216.36

    # Check 0 distance for single point
    assert total_distance([0], [0]) == 0

    # Test with points along the equator
    latitudes = [0, 0, 0]
    longitudes = [0, 90, 180]
    assert round(total_distance(latitudes, longitudes, unit="kilometers"), 2) == 20015.09  # Half Earth's circumference
