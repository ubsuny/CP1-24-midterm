"""
This module contains functions to find the direction of motion from acceleration data
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def direction_of_motion(ax,ay,az,t, i, v_0):
    '''
    This function plots the direction of motion at a given time, t[i] given acceleration data.

    Parameters:
    - t: Time values at which we have a defined acceleration and at which we will find the velocity
    - ax: x-acceleration at each time, t
    - ay: y-acceleration at each time, t
    - az: z-acceleration at each time, t
    - i: index of t at which we find the direction of motion
    - v_0: Initial velocity assumed to be the same in all direction. Generally zero.

    Returns:
    - 3d plot of normalized vector v 
    '''

    vx = velocity(t,ax,v_0)
    vy = velocity(t,ay,v_0)
    vz = velocity(t,az,v_0)

    v_mag = np.sqrt(vx**2+vy**2+vz**2)

   # Plot vectors using quiver
    ax.quiver(0, 0, 0, vx[i], vy[i], vz[i], color='b', length=1, normalize=True)

    # Label axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    v = max(vx[1], vy[1], vz[1])/v_mag

    ax.set_xlim([-v, v])  # Set the range for x-axis
    ax.set_ylim([-v, v])  # Set the range for y-axis
    ax.set_zlim([-v, v])

    plt.show()
