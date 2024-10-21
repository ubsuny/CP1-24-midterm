import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import math as m

walk = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/walktest.csv')

"""print(walk)"""

"""for the test the horizontal accuracy was 4.7 m, and verticle accuracy was 3.4"""

def walkeq(walkdt):
    len = walkdt.shape[0]
    """walkt = list(walkdt.loc[:, 'Time (s)'])"""
    laloalt = list(zip(walkdt.loc[:, 'Latitude (°)'], walkdt.loc[:, 'Longitude (°)'], walkdt.loc[:, 'Altitude WGS84 (m)']))
    a = 6378000
    f = 1/(298.3)
    b=(1-f)*a
    u = np.zeros(len)
    phi = np.zeros(len)
    l=abs(laloalt[0][1]-laloalt[1][1])
    s = np.zeros(len)

    for i in range(len-1):
        phi[i]=laloalt[i][0]
        u[i] = m.atan((1-f)*m.tan(phi[i]))

    for i in range(len-1):
        lam = l
        while lam > 10**(-5):
            sio=((m.cos(u[i+1])*m.sin(lam))**2+(m.cos(u[i])*m.sin(u[i+1])-m.sin(u[i])*m.cos(u[i+1])*m.cos(lam))**2)**(1/2)
            coo=m.sin(u[i])*m.sin(u[i+1])+m.cos(u[i])*m.cos(u[i+1])*m.cos(lam)
            sig=m.atan2(sio,coo)
            alp=m.asin((m.cos(u[i])*m.cos(u[i+1])*m.sin(lam))/(m.sin(sig)))
            sigm=0.5*m.acos(m.cos(sig)-2*(m.sin(u[i])*(m.sin(u[i+1])))/(m.cos(alp)**2))
            c=f*(m.cos(sig)**2)*(4+f*(4-3*(m.cos(alp)**2)))/16
            lam=l+(1-c)*f*(m.sin(sig))*(sig+c*m.sin(sig)*(m.cos(2*sigm)+c*m.cos(sig)*(2*(m.cos(2*sigm)**2)-1)))

        litu=((m.cos(alp))**2)*((a**2-b**2)/(b**2))
        biga=1+((u**2)/16384)*(4096+(litu**2)*((litu**2)*(320-175*(litu**2))-768))
        bigb=((litu**2)/1024)*(256+(litu**2)*((litu**2)(74-47*(litu**2))-128))
        dsig=bigb*m.sin(sig)*(m.cos(2*sigm)+0.25*bigb*(m.cos(sig)*(2*(m.cos(2*sigm))**2-1)-(1/6)*bigb*m.cos(2*sigm)*(4*(m.sin(sig)**2)-3)*(4*(m.cos(2*sigm)**2)-3)))
        s[i+1]=b*biga*(sig-dsig)
    return s

print(walkeq(walk))