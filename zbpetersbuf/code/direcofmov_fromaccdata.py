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
    plt.figure(vel[0][:,0], vel[1])

