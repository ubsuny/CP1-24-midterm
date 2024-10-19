"""
code_tobenamedlatter.py

note to self
import pandas as pd
df = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/tes_data.csv')

"""
import numpy as np

def imptomec(x,lenguni):
    if lenguni == 'yard':
        x = 3*x
    return 0.305*x

import pandas as pd
df = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/tes_data.csv')

print(df)


eupdata = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL001_elevatorup.cvs')
edowndata = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL002_elevatordown.cvs')