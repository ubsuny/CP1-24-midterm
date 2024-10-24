"""
This module contains functions to find the direction of motion from acceleration data
"""

import numpy as np


def velocity(t, a, v_0):
    '''
    This function calculates velocity given a time range, 
    acceleration at each instance of time, and an initial velocity

    Parameters:
    - t: Time values at which we have a defined acceleration and at which we will find the velocity
    - a: acceleration at each time, t
    - v_0: Initial velocity. Generally zero.

    Returns:
    - v: Velocity at each time t
    '''

    #Calculate the time step differences
    dt = np.diff(t, prepend=t[0])
    #Perform cumulative trapezoidal integration over acceleration to get velocity
    v = v_0 + np.cumsum(a * dt)
    return v

def direction_of_motion(ax,ay,az,t, v_0):
    '''
    This function calculates direction of motion given a time range, 
    acceleration at each instance of time in each of the three coordinate axes, and an initial velocity

    Parameters:
    - t: Time values at which we have a defined acceleration and at which we will find the velocity
    - ax: x-acceleration at each time, t
    - ay: y-acceleration at each time, t
    - az: z-acceleration at each time, t
    - v_0: Initial velocity. Generally zero.

    Returns:
    - dom: direction of motion at each time t as unit vector pointing in the same direction as velocity vector
    '''

    vx = velocity(t,ax,v_0)
    vy = velocity(t,ay,v_0)
    vz = velocity(t,az,v_0)

    v_mag = np.sqrt(vx**2+vy**2+vz**2)

    dom = []

    # Iterate through velocity magnitudes and calculate direction of motion
    for i, vm in enumerate(v_mag):
        if vm == 0:
            dom.append('Undefined')  # Add 'Undefined' if the velocity magnitude is zero
        else:
            # Normalize the velocity vector and append it to the dom list
            dom.append(np.array([vx[i], vy[i], vz[i]]) / vm)

    return dom
