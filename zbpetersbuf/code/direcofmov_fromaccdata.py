"""
direcofmov_fromaccdata.py

note to self
import pandas as pd
df = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/tes_data.csv')

"""
import pandas as pd
import numpy as np

df = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/tes_data.csv')
print(df)

eupdata = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL001_elevatorup.cvs')
edowndata = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL002_elevatordown.cvs')