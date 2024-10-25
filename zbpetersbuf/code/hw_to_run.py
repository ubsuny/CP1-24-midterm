"""
mak_plts.py
This module can be ran to the get the plot for the elevator velocities
and position plots for the circle and triangle

in the file elevator.py

how to use the function dimotion 
Enter the acceleration without g data in here, it then exports the time and velocities for
the x y and z in two maxtresies, combined into one. too access the time matrix to acces the time 
matrix do dimotion(edata)[1] the matrix data is dimotion(edata)[0] where the x velocity is
accessed by dimotion(edata)[0][:,0], y is dimotion(edata)[0][:,1]
and z is dimotion(edata)[0][:,2]

how to use the function pldimot
This function takes in the data that dimotion exports (ie pldimot(dimotion(edata))) and
graphs the 3 velocities on one graph also once the function is used in your comand line it
asks if you want ot save your data, if you dont type yes nothing happens and the graph is not
saved, if you typoe yes the terminal then askes where in your directery you want to save the
.png file, ie if you want to save in in the code file enter
/workspaces/CP-24-midterm/zbpetersbuf/code/ it then saves the .png in this folder as Elevator
velocities.png if a file already existes with that name in the folder it overwrites
the save and saves the most recent image

in the file imp_to_metr.py

how to use the function imptomec
Enter your mesurement value and then the kind of mesurment, ie if feet enter ft, feet or foot
if its yards enter yards, yard it then gives the equivelent value in meters

in the file uniti_con.py

how to use the function gt_unix
this code finds the time and data in the .md files for each data .csv
file and converts then exports the time in unixt time ie unix time converter

in the file workinh.py

how to use the function walkeq

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
plwalk(datforgraf,"Behold a circle","walking_cir.png")

triwalk = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL09_triangle.csv')
trwal = gpsloc(triwalk)
plwalk(trwal,"Walking in a triangle near the bus stop","walking_tri.png")
