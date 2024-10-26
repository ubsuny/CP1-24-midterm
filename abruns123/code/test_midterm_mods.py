"""
the test_midterm_mods module includes
test functions to verify that the other
modules are functioning as intended via
pytest used with the commandline.
"""
import numpy as np
from unit_converter import ft_to_m, yd_to_m
from unix_time import years, time, time_reader,date_reader
from distance_calc import diffm, reader
from abruns123.code.direction_of_motion import get_direction, acc_reader

def test_ft_to_m():
    """
    test_fit_to_m verifies that the 
    function successfully carries out 
    unit conversion from feet to meters
    """
    np.testing.assert_allclose(ft_to_m(1),(.3048))

def test_yd_to_m():
    """
    test_fit_to_m verifies that the 
    function successfully carries out 
    unit conversion from yards to meters
    """
    np.testing.assert_allclose(yd_to_m(1), .9144)

def test_years():
    """
    test_years verifies that the 
    years function can accurately
    create lists of length corresponding
    to the number of leap years and 
    non-leap years between 1970 and the 
    input year. 
    """
    ny,ly=years(2130)
    assert len(ny)==121
    assert len(ly)==39

def test_time():
    """
    test_time uses a known unix time 
    taken from the unix timestamp
    website and verifies that
    the time function calculates the correct
    unix time.
    """
    #Test is based on comparison with test value used 
    #on unix timestamp website
    #citation: [1][1] Unix Time Stamp - Epoch Converter. (n.d.). 
    # https://www.unixtimestamp.com/
    date=[2024,10,24,17,45,53]
    assert time(date)==1729806353

def test_diffm():
    """
    test_diffm confirms that diffm
    returns an object with length 2.
    This is important as there need to 
    be two indices to represent x and y
    """
    lat1=43.008895100
    lat2=43.008135760
    lon1=-78.785005700
    lon2=-78.784864890
    assert len(diffm(lat1,lat2,lon1,lon2))==2

def test_reader():
    """
    test reader verifies that the various reader functions 
    can run without producing an error in the case that a 
    file without the data they're meant to read is the input.
    """
    reader("/AB123/data/Triangle Data/time.csv")
    time_reader("/AB123/data/Triangle Data/time.csv")
    date_reader("/AB123/data/Triangle Data/Location.csv")
    acc_reader("/AB123/data/Triangle Data/time.csv")

def test_direction():
    """
    test_direction verifies that the start and end behaviors
    of the two elevator experiments are as expected
    """
    acc,times=acc_reader("/AB123/data/down_data/Raw Data.csv")
    directions=get_direction(times, acc)
    assert directions[0]==0
    assert directions[len(directions)-1]==0

    acc,times=acc_reader("/AB123/data/up_data/Raw Data.csv")
    directions=get_direction(times, acc)
    assert directions[0]==0
    assert directions[len(directions)-1]==0
