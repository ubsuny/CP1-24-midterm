import pytest
from unixtime_converter import (
    read_text_metafile,
    is_leap_year,
    days_in_month,
    convert_to_unix_time,
    get_unix_time_from_metafile
)

# Test if the leap year function works as expected
def test_is_leap_year():
    assert is_leap_year(2020) == True  # Leap year
    assert is_leap_year(2019) == False  # Not a leap year
    assert is_leap_year(2000) == True  # Divisible by 400
    assert is_leap_year(1900) == False  # Divisible by 100, but not 400

# Test if the function returns correct days in a month
def test_days_in_month():
    assert days_in_month(2, 2020) == 29  # February in leap year
    assert days_in_month(2, 2019) == 28  # February in non-leap year
    assert days_in_month(1, 2020) == 31  # January
    assert days_in_month(4, 2020) == 30  # April

def test_convert_to_unix_time():
    assert convert_to_unix_time('1970-01-01', '00:00:00') == 0  # Epoch time
    assert convert_to_unix_time('1970-01-02', '00:00:00') == 86400  # One day after epoch
    assert convert_to_unix_time('2024-10-21', '14:30:00') == 1729521000  # Updated correct timestamp

def test_get_unix_time_from_metafile(tmpdir):
    # Create a temporary metafile for testing
    metafile = tmpdir.join("test_metadata.txt")
    metafile.write("Date: 2024-10-21\nTime: 14:30:00")
    
    unix_time = get_unix_time_from_metafile(str(metafile))
    assert unix_time == 1729521000  # Updated correct timestamp

# Test reading the metafile and parsing it correctly
def test_read_text_metafile(tmpdir):
    # Create a temporary file using pytest's tmpdir fixture
    metafile = tmpdir.join("test_metadata.txt")
    metafile.write("Date: 2024-10-21\nTime: 14:30:00")

    expected_metadata = {
        'Date': '2024-10-21',
        'Time': '14:30:00'
    }
    result = read_text_metafile(str(metafile))
    assert result == expected_metadata

