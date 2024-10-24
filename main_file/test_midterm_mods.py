import pytest
import numpy as np
from unit_converter import ft_to_m, yd_to_m
from unix_time import years
from main_file.distance2 import diffm, reader

def test_ft_to_m():
    np.testing.assert_allclose(ft_to_m(1),(.3048)) 

def test_yd_to_m():
    np.testing.assert_allclose(yd_to_m(1), .9144)

def test_years():
    ny,ly=years(2130)
    assert len(ny)==121
    assert len(ly)==39

def test_diffm():
    lat1=43.008895100
    lat2=43.008135760
    lon1=-78.785005700
    lon2=-78.784864890
    print(diffm(lat1,lat2, lon1,lon2))
    assert (np.sqrt(diffm(lat1,lat2,lon1,lon2)[0]**2+diffm(lat1,lat2,lon1,lon2)[1]**2))>.5

def test_file():
    reader("/workspaces/CP1-24-midterm/main_file/Triangle Data/Location.csv")