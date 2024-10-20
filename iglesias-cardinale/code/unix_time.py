"""
This module converts time given in year, month, day, hour, minute, second format into UNIX time. 
Unix time is a time measurement measuring the number of elapsed seconds since January 1, 1970
"""

def yearshift(year):
    '''
    Calculates the number of years between the year for which we're calculating UNIX time and 1970

    Pararmeters:
    - year: The year we for which we are finding UNIX time

    Returns:
    - year - 1970
    '''
    return year - 1970

def month2year(month):
    '''
    Calculates the number of days in the year up to the given month 
    as a fraction of the number of days in a year

    Parameters:
    - month: month of interest. Must be 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, or 12.
    
    Returns:
    - v: Number of days from the beginning of the year to the beginnning of the month 
    as a fraction of the number of days in a year
    '''
    if month == 1:
        v = 0
    elif month == 2:
        v = 31
    elif month == 3:
        v = 59
    elif month == 4:
        v = 90
    elif month == 5:
        v = 120
    elif month == 6:
        v = 151
    elif month == 7:
        v = 181
    elif month == 8:
        v = 212
    elif month == 9:
        v = 243
    elif month == 10:
        v = 273
    elif month == 11:
        v = 304
    elif month == 12:
        v = 334

    return v/365

def day2year(day):
    '''
    Calculates the fraction of a year in the number of days in the given date

    Parameters:
    - day: the day of the month 

    Returns:
    - The fraction of a year taken up by the given number of days 
    '''

    return day/365


def hour2year(hour):
    '''
    Calculates the fraction of a year in the number of hours in the given date

    Parameters:
    - hour: the hour of the day 

    Returns:
    - The fraction of a year taken up by the given number of hours 
    '''

    return hour/(24*365)

def minute2year(minute):
    '''
    Calculates the fraction of a year in the number of minutes in the given date

    Parameters:
    - minute: the minute of the hour of the day 

    Returns:
    - The fraction of a year taken up by the given number of minutes 
    '''

    return minute/(60*24*365)

def second2year(second):
    '''
    Calculates the fraction of a year in the number of seconds in the given date

    Parameters:
    - seconds: the number of seconds elapsed after the given minute value 

    Returns:
    - The fraction of a year taken up by the given number of seconds 
    '''

    return second/(60*60*24*365)

def date2unix(year, month, day, hour, minute, second):
    """
    Calculates the number of seconds elapsed between January 1, 1970 and the given date

    Parameters: 

    Returns:
    """

    yr = (year + month2year(month) + day2year(day) + hour2year(hour)
          + minute2year(minute) + second2year(second))

    yr_since_1970 = yearshift(yr)

    return yr_since_1970*60*60*24*365
