# motion_direction.py
import math

def calculate_direction(x, y, z):
    """Calculate the direction of motion from acceleration components.
    
    Args:
        x (float): Acceleration in the x-axis (m/s^2).
        y (float): Acceleration in the y-axis (m/s^2).
        z (float): Acceleration in the z-axis (m/s^2).
        
    Returns:
        float: Direction of motion in degrees from the x-axis in the xy-plane.
    """
    xy_direction = math.degrees(math.atan2(y, x))
    return xy_direction
