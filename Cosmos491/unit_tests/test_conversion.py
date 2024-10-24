import pytest
from your_module import feet_to_meters, yards_to_meters  # Replace 'your_module' with your actual module name

def test_feet_to_meters():
    assert feet_to_meters(1) == 0.3048  # 1 foot = 0.3048 meters
    assert feet_to_meters(10) == 3.048  # 10 feet = 3.048 meters
    assert feet_to_meters(0) == 0       # 0 feet should return 0 meters
    assert feet_to_meters(-5) == -1.524  # Negative value for edge case

def test_yards_to_meters():
    assert yards_to_meters(1) == 0.9144  # 1 yard = 0.9144 meters
    assert yards_to_meters(50) == 45.72  # 50 yards = 45.72 meters
    assert yards_to_meters(0) == 0       # 0 yards should return 0 meters
    assert yards_to_meters(-10) == -9.144  # Negative value for edge case
