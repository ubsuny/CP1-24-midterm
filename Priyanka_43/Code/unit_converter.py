# unit_converter.py

def feet_to_meters(feet):
    """
    Convert feet to meters.
    """
    if feet < 0:
        raise ValueError("Feet value cannot be negative.")
    return feet * 0.3048

def yards_to_meters(yards):
    """
    Convert yards to meters.
    """
    if yards < 0:
        raise ValueError("Yards value cannot be negative.")
    return yards * 0.9144
