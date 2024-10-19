"""
direcofmov_fromaccdata.py

l = eup.shape[0]-1

print(l)
print(eup)
print(eup.loc[0, 'Linear Acceleration x (m/s^2)'])

import pandas as pd
import numpy as np
eup = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL01_eupdata.csv')
edn = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL02_edndata.csv')

print(eup[1][1])
l = eup.shape[0]-1
vel = np.zeros((l, 4))

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def dimotion(edata):
    len = edata.shape[0]
    edat = list(edata.loc[:, 'Time (s)'])
    edaxyz = list(zip(edata.loc[:, 'Linear Acceleration x (m/s^2)'], edata.loc[:, 'Linear Acceleration y (m/s^2)'], edata.loc[:, 'Linear Acceleration z (m/s^2)']))
    vel = np.zeros((len, 3))
    for j in range(3):
        for i in range(len-1):
            if i == 0:
                t = edat[i]
            else:
                t = edat[i]-edat[i-1]
            vel[i+1,j]= vel[i,j] + t*edaxyz[i][j]
    return vel,edat



def pldimot(vel):
    plt.figure()

    vel_df = pd.DataFrame(vel[0])
    tim = vel_df.iloc[0].values

    plt.figure(tim[:], vel[1], marker='o')
    plt.title('xdir')
    plt.xlabel('t?')
    plt.ylabel('y?')
    plt.grid()
    plot = input("Do you want to save the plot? (yes/no): ").strip().lower()

    if plot == 'yes':
        fpath = input("enter where to save: ").strip()
        if not os.path.exists(fpath):
            print("Directory does not exist, try again")
        else:
            filpath = os.path.join(fpath, "plot.png")
            plt.savefig(filpath, format='png')
            print(f"Plot saved as {filpath}")
    else:
        print("Plot not saved.")


