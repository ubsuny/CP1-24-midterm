"""

import matplotlib.pyplot as plt
import os

for the test the horizontal accuracy was 4.7 m, and verticle accuracy was 3.4
"""

import math as m
import numpy as np
import pandas as pd

def walkeq(walkdt):
    """docstring type words here"""

    laloalt = list(zip(walkdt.loc[:, 'Latitude (°)'],
                        walkdt.loc[:, 'Longitude (°)'], walkdt.loc[:, 'Altitude WGS84 (m)']))

    u = np.zeros(walkdt.shape[0])
    s = np.zeros(walkdt.shape[0])

    for i in range(walkdt.shape[0]):
        u[i] = np.radians(m.atan((1-(np.radians(1/(298.257))))*m.tan(np.radians(laloalt[i][0]))))

    for i in range(walkdt.shape[0]-1):
        lam = np.radians(abs(laloalt[0][1]-laloalt[1][1]))
        lamp=0
        while abs(abs(lam) - abs(lamp)) > 10**(-12):
            lamp = lam
            sig=m.atan2(((m.cos(u[i+1])*m.sin(lam))**2+(m.cos(u[i])*
                    (m.sin(u[i+1]))-(m.sin(u[i]))*(m.cos(u[i+1]))*(m.cos(lam)))**2)**(1/2),
                        (m.sin(u[i]))*(m.sin(u[i+1]))+(m.cos(u[i]))*(m.cos(u[i+1]))*(m.cos(lam)))
            alp=m.asin((m.cos(u[i])*(m.cos(u[i+1]))*(m.sin(lam)))/(m.sin(sig)))
            sigm=0.5*m.acos(m.cos(sig)-2*(m.sin(u[i])*(m.sin(u[i+1])))/(m.cos(alp)**2))
            c=(np.radians(1/(298.257)))*(m.cos(sig)**2)*(4+(np.radians(1/(298.257)))*
                    (4-3*(m.cos(alp)**2)))/16
            lam=abs(laloalt[0][1]-laloalt[1][1])+(1-
                    c)*(np.radians(1/(298.257)))*(m.sin(sig))*(sig+c*m.sin(sig)*
                        (m.cos(2*sigm)+c*m.cos(sig)*(2*(m.cos(2*sigm)**2)-1)))

        litu=((m.cos(alp))**2)*(((np.radians(6378140))**2-((1-(np.radians(1
                /(298.257))))*np.radians(6378140))**2)/(((
                    1-(np.radians(1/(298.257))))*np.radians(6378140))**2))**2
        biga=1+((u[i]**2)/16384)*(4096+(litu)*((litu)*(320-175*(litu))-768))
        bigb=((litu)/1024)*(256+(litu)*((litu)*(74-47*(litu))-128))
        dsig=(bigb*m.sin(sig))*(m.cos(2*sigm)+0.25*bigb*(m.cos(sig)*
                (2*(m.cos(2*sigm))**2-1)-(1/6)*bigb*m.cos(2*sigm)*(4*
                    (m.sin(sig)**2)-3)*(4*(m.cos(2*sigm)**2)-3)))
        s[i+1]=((1-(np.radians(1/(298.257))))*np.radians(6378140))*biga*(sig-dsig)
    return s

walk = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL07_circle.csv')
print(walkeq(walk))
print(sum(walkeq(walk)))
