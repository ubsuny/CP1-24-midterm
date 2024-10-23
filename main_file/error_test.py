import numpy as np
import unit_converter
import pandas as pd

def get_coords(d,xy,i):
    if i!=0:
        xy+=get_coords(d, d[i], i-1)
    if i==0:
        return xy

def diff(lat1,lat2, lon1,lon2):
    lat1, lat2=lat1*364000,lat2*364000
    lon1, lon2=lon1*288200,lon2*288200
    return np.array([(lon2-lon1),(lat2-lat1)])

def diffm(lat1, lat2,lon1, lon2):
    return unit_converter.ft_to_m(diff(lat1,lat2, lon1, lon2))

def reader(path):
    file=pd.read_csv(path)
    lats=file["Latitude (°)"]
    lons=file["Longitude (°)"]
    return lats, lons