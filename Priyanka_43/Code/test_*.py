'''
unit testing module for unit_converter.py
'''
import pytest

from unit_converter import feet_to_metres, yards_to_metres

def test_feet_to_metres():
    '''
    function to test the foot to metre conversion
    '''
    assert feett_to_metres(1) == 0.3048   # checking if 1 foot = 0.3048 metre or not
  
def test_yards_to_metres():
    '''
    function to test the yards to metres conversion
    '''
    assert yards_to_metres(1) == 0.9144   # checking if 1 yard = 0.9144 metre or not

'''
unit testing module for motion_direction.py
'''
from motion_direction import calculate_direction

def test_calcualte_direction():
    """Tests for acceleration along the x and y axes"""
    # Test for acceleration along the x-axis
    theta, phi = calculate_direction(1, 0, 0)
    assert pytest.approx(theta, 0.1) == 90  # Polar angle θ
    assert pytest.approx(phi, 0.1) == 0     # Azimuthal angle φ

    # Test for acceleration along the z-axis
    theta, phi = calculate_direction(0, 0, 1)
    assert pytest.approx(theta, 0.1) == 0   # Polar angle θ



