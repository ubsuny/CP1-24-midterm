"""
This module contains functions to find the direction of motion from acceleration data
"""

import numpy as np


def velocity(a, v0, t):
    '''
    Calculates the direction of motion as the normalized velocity vector at each instance of time

    parameters:
    - a: 3xN array like acceleration data
    - v0: float like initial velocity. Usually zero.
    - t: 1xN array like time data 

    returns:
    - v_norm: array like normalized 
    '''
    dt = (t[-1]-t[0])/len(t)

    v = v0 + [(a[i+1]-a[i])*dt for i in len(a)]

    v_norm = v/np.sqrt(np.sum(v**2))
    return v_norm
