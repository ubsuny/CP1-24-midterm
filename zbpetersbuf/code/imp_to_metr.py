"""
code_tobenamedlatter.py

import pandas as pd
import numpy as np
eup = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL01_eupdata.csv')
edn = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL02_edndata.csv')

l = eup.shape[0]-1
vel = np.zeros((l, 4))
vel[0,1]=1
edat=list(eup.loc[:,'Time (s)'])
print(edat[0]*2)

"""
import numpy as np
import pandas as pd
import math

def imptomec(x,lenguni):
    if lenguni == 'yard' or 'yd':
        x = 3*x
    return 0.305*x

walk = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/walktest.csv')
laloalt = list(zip(walk.loc[:, 'Latitude (°)'], walk.loc[:, 'Longitude (°)'], walk.loc[:, 'Altitude WGS84 (m)']))
print(walk)
print(laloalt[1][1])
print(abs(-1))
math.acos