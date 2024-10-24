"""
test_elevator.py
this moduale is the unit test for elevator.py
"""
import pandas as pd
import numpy as np
from elevator import dimotion

dta = pd.DataFrame([['Time (s)','Linear Acceleration x (m/s^2)','Linear Acceleration y (m/s^2)','Linear Acceleration z (m/s^2)'],[1,3,3,3],[2,1,2,2],[3,1,2,3]])

def func():
    a = [[0,0,0],[3,3,3],[4,5,5]]
    b = [1,2,3]
    return np.array(a), b
v_and_t = func()

def test_imptomec():
    result = dimotion(dta)
    """This tests the ohmscur function"""
    assert result[1] == v_and_t[1]
