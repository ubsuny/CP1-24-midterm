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

def imptomec(x,lenguni):
    if lenguni == 'yard' or 'yd':
        x = 3*x
    return 0.305*x

