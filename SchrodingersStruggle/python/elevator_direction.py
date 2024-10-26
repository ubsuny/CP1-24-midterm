"""
This module imports data from a csv file and calculates direction
of motion in each cartesian direction from elevator data.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def acceleration(csv_file):
    """
    Gathers accelerations in x, y, and z direction and combines them into one list. 
    Also gathers times from csv file provided.
    - File must have headers with the exact headers shown.
    - Uses pandas to read csv, and .values to only export the data.
    """
    try:
        open_file = pd.read_csv(csv_file)
        accelerations = []
        accel_x = open_file['Linear Acceleration x (m/s^2)'].values
        accel_y = open_file['Linear Acceleration y (m/s^2)'].values
        accel_z = open_file['Linear Acceleration z (m/s^2)'].values
        accelerations.append(accel_x)
        accelerations.append(accel_y)
        accelerations.append(accel_z)
        times = open_file['Time (s)'].values
    except FileNotFoundError:
        print('File was not found')
    except KeyError:
        print("File must have 'Linear Acceleration y (m/s^2)', and 'Time (s)' headers.")
    return accelerations, times

def velocity(accelerations, times):
    """
    Produces the velocities in x y z cooresponding to a time.
    - Estimated velocity by taking the acceleration at a given point,
      the time between that reading and the next, and multiplying
      the acceleration by that change in time.
    - Data omits the first time, as it is negative, and
      the final acceleration, since there is no time for it to
      change the velocity.
    """
    velocities_x = [0]
    velocities_y = [0]
    velocities_z = [0]
    velocities = []
    times_mod = []
    for i in range(1,len(accelerations[0])):
        velocity_change = accelerations[0][i-1]*(times[i]-times[i-1])
        velocities_x.append(velocity_change + velocities_x[i-1])
        times_mod.append(times[i])
    for i in range(1,len(accelerations[1])):
        velocity_change = accelerations[1][i-1]*(times[i]-times[i-1])
        velocities_y.append(velocity_change + velocities_y[i-1])
    for i in range(1,len(accelerations[2])):
        velocity_change = accelerations[2][i-1]*(times[i]-times[i-1])
        velocities_z.append(velocity_change + velocities_z[i-1])
    velocities.append(velocities_x)
    velocities.append(velocities_y)
    velocities.append(velocities_z)
    return velocities

def movement_directions(velocities):
    """
    Obtains vectorized form of velocity in spherical coordinates, to show magnitude and
    direction of total velocity.
    """
    if not isinstance(velocities, list):
        raise TypeError("Inputs should be in the form of int, float, or list.")
    if len(velocities) != 3:
        raise TypeError("Velocities should be list of dimension 3.")
    vel_r = []
    vel_theta = []
    vel_phi = []
    vectors_sphere = []
    for i in range(0,len(velocities[0])):
        x = velocities[i,0]
        y = velocities[i,1]
        z = velocities[i,2]
        mag = np.linalg.vector_norm([x,y,z])
        if mag == 0:
            mag = theta = phi = 0
        if x == 0:
            theta = np.pi/2
            phi = np.arccos(z/mag)
        else:
            theta = np.mod(np.arctan2(y,x), 2*np.pi)
            phi = np.arccos(z/mag)
        vel_r.append(mag)
        vel_theta.append(theta)
        vel_phi.append(phi)
    vectors_sphere.append(vel_r)
    vectors_sphere.append(vel_theta)
    vectors_sphere.append(vel_phi)
    return vectors_sphere

#Testing:
ACCELERATIONS, TIMES= acceleration('your_data_path_here.csv')
VELOCITIES = velocity(ACCELERATIONS, TIMES)
plt.figure()
plt.plot(TIMES, VELOCITIES[0], color = 'r', label = 'x-axis')
plt.plot(TIMES, VELOCITIES[1], color = 'b', label = 'y-axis')
plt.plot(TIMES, VELOCITIES[2], color = 'g', label = 'z-axis')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.xlim()
plt.ylim()
plt.title('Velocity of Elevator vs. Time')
plt.show()
plt.savefig('save_file_here.png',dpi = 300)
plt.close()
