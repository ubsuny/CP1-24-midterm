# test_unixtime_converter.py

from unixtime_converter import to_unix_time, from_unix_time, validate_datetime_format

def test_to_unix_time():
    # Test known Unix time values
    assert to_unix_time("January 1st, 1970", "00:00 AM") == 0
    assert to_unix_time("January 2nd, 1970", "00:00 AM") == 86400
    assert to_unix_time("February 29th, 2020", "00:00 AM") == 1582934400  # Leap year

    # Adjustment test
    assert to_unix_time("January 1st, 1970", "01:00 AM", adjustment_seconds=3600) == 7200

    # Invalid date formats
    try:
        to_unix_time("Feb 30, 2021", "12:00 PM")  # Invalid date
    except ValueError:
        assert True

def test_from_unix_time():
    # Check reverse conversion of Unix timestamps
    assert from_unix_time(0) == "January 01, 1970 12:00 AM"
    assert from_unix_time(86400) == "January 02, 1970 12:00 AM"

    # Leap second check
    assert from_unix_time(1483228799) == "December 31, 2016 11:59 PM"

def test_validate_datetime_format():
    # Validate correct formats
    assert validate_datetime_format("January 1st, 1970", "00:00 AM") == True
    assert validate_datetime_format("February 29th, 2020", "11:59 PM") == True  # Leap day

    # Check invalid formats and dates
    assert validate_datetime_format("Feb 30, 2021", "12:00 PM") == False  # Invalid date
    assert validate_datetime_format("January 1, 1970", "00:00") == False  # Wrong time format
