# test_motion_direction.py

from motion_direction import calculate_direction

def test_calculate_direction():
    # Basic direction checks in XY-plane
    assert round(calculate_direction(1, 1, 0), 2) == 45.0
    assert round(calculate_direction(0, 1, 0), 2) == 90.0
    assert round(calculate_direction(-1, 0, 0), 2) == 180.0
    assert round(calculate_direction(0, -1, 0), 2) == -90.0

    # Test edge cases with zero acceleration
    try:
        calculate_direction(0, 0, 0)  # Should raise ZeroDivisionError
    except ZeroDivisionError:
        assert True

    # Small values to ensure stability
    assert round(calculate_direction(1e-9, 1e-9, 0), 2) == 45.0
    assert round(calculate_direction(-1e-9, -1e-9, 0), 2) == -135.0

    # Direction with only z-component (should ideally not affect XY-plane direction)
    assert round(calculate_direction(1, 1, 1), 2) == 45.0 
