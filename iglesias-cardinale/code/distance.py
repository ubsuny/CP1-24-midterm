"""
This module contains functions to find distances between two GPS positions
"""

def gps_flat_earth(x1,x2):
    '''
    Calculates the absolute distance between two adjacent gps points assuming a flat Earth

    Parameters:
    - x1: List of values containing the x, y and z values of the first position. 
          Should have the same units as x2.
    - x2: List of values containing the x, y and z values of the second position.
          Should have the same units as x1.

    Returns:
    - Absolute distance between x1 and x2 in the same units as x1 and x2
    '''

    return (sum((x2[i]-x1[i])**2 for i in len(x1)))**0.5
