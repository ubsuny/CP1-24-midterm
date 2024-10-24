"""
elevator.py
This module contains the code necessary to interpret the data collected from the
elevator data collection
"""
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def dimotion(edata):
    """Enter the acceleration without g data in here, it then exports the time and velocities for
    the x y and z in two maxtresies, combined into one. to acces the time matrix to acces the time 
    matrix do dimotion(edata)[1] the matrix data is dimotion(edata)[0] where the x velocity is
    accessed by dimotion(edata)[0][:,0], y is dimotion(edata)[0][:,1]
    and z is dimotion(edata)[0][:,2]"""
    edat = list(edata.loc[:, 'Time (s)'])
    edaxyz = list(zip(edata.loc[:, 'Linear Acceleration x (m/s^2)'],
            edata.loc[:, 'Linear Acceleration y (m/s^2)'],
                edata.loc[:, 'Linear Acceleration z (m/s^2)']))
    vel = np.zeros((edata.shape[0], 3))
    for j in range(3):
        for i in range(edata.shape[0]-1):
            if i == 0:
                t = edat[i]
            else:
                t = abs(edat[i]-edat[i-1])
            vel[i+1,j]= vel[i,j] + t*edaxyz[i][j]
    return vel,edat

def pldimot(vel):
    """This function takes in the data that dimotion exports (ie pldimot(dimotion(edata))) and
    graphs the 3 velocities on one graph also once the function is used in your comand line it
    asks if you want ot save your data, if you dont type yes nothing happens and the graph is not
    saved, if you typoe yes the terminal then askes where in your directery you want to save the
    .png file, ie if you want to save in in the code file enter
    /workspaces/CP-24-midterm/zbpetersbuf/code/ it then saves the .png in this folder as Elevator
    velocities.png if a file already existes with that name in the folder it overwrites
    the save and saves the most recent image"""
    plt.figure()
    vel_df = pd.DataFrame(vel[0])
    vmovx = vel_df.iloc[:,0].values
    vmovy = vel_df.iloc[:,1].values
    vmovz = vel_df.iloc[:,2].values
    plt.plot(vel[1],vmovx, color='red', label='x velocity')
    plt.plot(vel[1],vmovy, color='blue', label='y velocity')
    plt.plot(vel[1],vmovz, color='g', label='z velocity')
    plt.title('Elevator velocity')
    plt.xlabel('Start from ground floor then up to top then backdown (s)')
    plt.ylabel('Velocity of moving elevator (m/s)')
    plt.legend()
    plt.grid()
    plot = input("Do you want to save the plot? (yes/no): ").strip().lower()

    if plot == 'yes':
        fpath = input("enter where to save: ").strip()
        if not os.path.exists(fpath):
            print("Directory does not exist, try again")
        else:
            filpath = os.path.join(fpath, "Elevator velocities.png")
            plt.savefig(filpath, format='png', dpi=300)
            print(f"Plot saved as {filpath}")
    else:
        print("Plot not saved.")
