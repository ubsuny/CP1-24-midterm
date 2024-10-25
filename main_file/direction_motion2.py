import numpy as np
import pandas as pd

def get_del_t(times):
    dt=[]
    for i in range(len(times)-1):
        dt.append(times[i+1]-times[i])
    sum=0
    for i in dt:
        sum+=i
    sum=sum/len(dt)
    dt.append(sum)
    return dt
def adjust_acc(acc):
    for i in range(len(acc)):
        if np.abs(acc[i])<.8:
            acc[i]=0
    return acc

def get_vel(a, dt, i):
    vel=0
    for j in range(i+1):
        vel+=a[j]*dt[j]
    return vel


def get_direction(times, acc):
    dt=get_del_t(times)
    acc=adjust_acc(acc)
    vel=[]
    for i in range(len(dt)):
        vel.append(get_vel(acc,dt,i))

    direction=[]
    for i in range(len(vel)):
        if vel[i]!=0:
            direction.append(vel[i]/(np.abs(vel[i])))
        else:
            direction.append(0)

    return direction

def acc_reader(path):
    file =pd.read_csv(path)
    acc=file["Linear Acceleration z (m/s^2)"]
    times=file["Time (s)"]
    return acc, times