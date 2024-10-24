"""
test_elevator.py
this moduale is the unit test for elevator.py
"""
from elevator import dimotion, pldimot
import pandas as pd

etot = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL05_eletot.csv')

vel = dimotion(etot)

pldimot(vel)
