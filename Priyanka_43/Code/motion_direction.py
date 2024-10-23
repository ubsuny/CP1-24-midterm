# motion_direction.py

import math

def calculate_direction(acceleration):
    """
    Calculate the direction of motion from acceleration data.

    Parameters:
    acceleration (tuple): A tuple containing the acceleration data (ax, ay, az)
                          in the x, y, and z directions.

    Returns:
    tuple: A normalized direction vector (dx, dy, dz).
    """
    ax, ay, az = acceleration

    # Calculate the magnitude of the acceleration vector
    magnitude = math.sqrt(ax**2 + ay**2 + az**2)

    if magnitude == 0:
        raise ValueError("Acceleration magnitude is zero; direction cannot be determined.")

    # Normalize the direction vector
    dx = ax / magnitude
    dy = ay / magnitude
    dz = az / magnitude

    return (dx, dy, dz)
