"""
code_tobenamedlatter.py

"""
import numpy as np

def imptomec(x,lenguni):
    if lenguni == 'yard':
        x = 3*x
    return 0.305*x

import tes_data.csv as pd

df = pd.read_csv('data.csv')
