import numpy as np
import pandas as pd

def get_del_t(times):
    dt=[]
    for i in range(len(times)-1):
        dt.append([times[i+1]-times[i]])
    sum=0
    for i in dt:
        sum+=i
    sum=sum/len(dt)
    dt.append(sum)
    return dt

def get_vel(a, dt, v, i):
    if i==0:
        return v
    return v+get_vel(a,dt,a[i-1]*dt[i-1],i-1)


def get_direction(times, acc):
    dt=get_del_t(times)
    vel=[]
    for i in range(len(dt)):
        vel.append(get_vel(acc,dt, acc[i]*dt[i],i))

    direction=[]
    for i in range(len(vel)):
        direction.append(vel[i]/(np.abs(vel[i])))

    return direction

def acc_reader(path):
    file =pd.read_csv(path)
    print(file)

    