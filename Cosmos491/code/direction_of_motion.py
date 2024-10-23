import numpy as np
def calculate_direction(acceleration_data):
    """
    Calculate the direction of motion based on acceleration data.

    Parameters:
    acceleration_data (list of lists): A list of [ax, ay, az] values representing 
    the acceleration in the x, y, and z axes.

    Returns:
    list of tuples: A list of normalized direction vectors in the form (dx, dy, dz).
    """
    directions = []
    for ax, ay, az in acceleration_data:
        magnitude = np.sqrt(ax**2 + ay**2 + az**2)
        if magnitude != 0:
            direction = (ax / magnitude, ay / magnitude, az / magnitude)
        else:
            direction = (0, 0, 0)
        directions.append(direction)
    return directions
