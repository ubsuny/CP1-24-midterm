# test_unit_converter.py

from unit_converter import feet_to_meters, yards_to_meters
import math

def test_feet_to_meters():
    # Basic conversions
    assert feet_to_meters(1) == 0.3048
    assert feet_to_meters(10) == 3.048
    assert feet_to_meters(0) == 0.0
    assert feet_to_meters(-1) == -0.3048  # Negative value test

    # Floating-point conversions
    assert round(feet_to_meters(5.5), 5) == 1.6764
    assert round(feet_to_meters(2.25), 5) == 0.6858

    # Large and small values
    assert feet_to_meters(1e6) == 304800  # Large value test
    assert feet_to_meters(1e-6) == 3.048e-7  # Small value test

    # Edge cases: infinity and NaN
    assert math.isinf(feet_to_meters(float('inf')))  # Test positive infinity
    assert math.isinf(feet_to_meters(float('-inf')))  # Test negative infinity
    assert math.isnan(feet_to_meters(float('nan')))  # Test NaN

def test_yards_to_meters():
    # Basic conversions
    assert yards_to_meters(1) == 0.9144
    assert yards_to_meters(10) == 9.144
    assert yards_to_meters(0) == 0.0
    assert yards_to_meters(-1) == -0.9144  # Negative value test

    # Floating-point conversions
    assert round(yards_to_meters(5.5), 5) == 5.0292
    assert round(yards_to_meters(2.25), 5) == 2.0574

    # Large and small values
    assert yards_to_meters(1e6) == 914400  # Large value test
    assert yards_to_meters(1e-6) == 9.144e-7  # Small value test

    # Edge cases: infinity and NaN
    assert math.isinf(yards_to_meters(float('inf')))  # Test positive infinity
    assert math.isinf(yards_to_meters(float('-inf')))  # Test negative infinity
    assert math.isnan(yards_to_meters(float('nan')))  # Test NaN
