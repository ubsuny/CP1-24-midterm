"""
mak_plts.py
This module can be ran to the get the plots for the elevator velocities
and position plots for the circle and triangle
"""
from elevator import dimotion, pldimot
from workinh import gpsloc, plwalk
import pandas as pd

etot = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL05_eletot.csv')
print(etot)
print([['Time (s)','Linear Acceleration x (m/s^2)','Linear Acceleration y (m/s^2)','Linear Acceleration z (m/s^2)'],[1,3,3,3],[2,1,2,2],[3,1,2,3]])
vel = dimotion(etot)
pldimot(vel)

walk = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL07_circle.csv')
datforgraf = gpsloc(walk)
plwalk(datforgraf)

triwalk = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL07_circle.csv')
datforgraf = gpsloc(walk)
plwalk(datforgraf)
