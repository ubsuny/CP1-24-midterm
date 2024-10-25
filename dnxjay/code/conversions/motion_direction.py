import math

def calculate_direction(x, y, z):
    """Calculate the direction of motion from x, y, z acceleration components."""
    xy_direction = math.degrees(math.atan2(y, x))
    return xy_direction
