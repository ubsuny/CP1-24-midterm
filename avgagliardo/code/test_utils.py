"""
Unit Conversion Module and Tests

This module provides a function `convert_to_meters` that converts various units
of length to meters. It supports common units such as kilometers, centimeters,
millimeters, inches, feet, yards, and miles.

The module also contains unit tests using `pytest` to verify the accuracy of
the conversion function. The tests cover a range of conversions and check for
correct error handling when an invalid unit is provided.

Functions:
    convert_to_meters(value, unit): Converts a given length from the specified
    unit to meters.

    import_csv

Test Cases:
    - Test conversion from kilometers to meters.
    - Test conversion from centimeters to meters.
    - Test conversion from millimeters to meters.
    - Test conversion from inches to meters.
    - Test conversion from feet to meters.
    - Test conversion from yards to meters.
    - Test conversion from miles to meters.
    - Test that an invalid unit raises a ValueError.

#TODO: ... Expand later

"""
import pytest
import pandas as pd
from utils import convert_to_meters
from utils import import_csv


class TestUnitConversion:
    """
    Test cases for the unit conversion functionality in convert_to_meters
    function.
    """

    def test_kilometers(self):
        """
        Test conversion from kilometers to meters.
        1 kilometer should equal 1000 meters.
        """
        assert convert_to_meters(1, 'km') == 1000

    def test_centimeters(self):
        """
        Test conversion from centimeters to meters.
        100 centimeters should equal 1 meter.
        """
        assert convert_to_meters(100, 'cm') == 1

    def test_millimeters(self):
        """
        Test conversion from millimeters to meters.
        1000 millimeters should equal 1 meter.
        """
        assert convert_to_meters(1000, 'mm') == 1

    def test_inches(self):
        """
        Test conversion from inches to meters.
        1 inch should equal exactly 0.0254 meters.
        """
        assert convert_to_meters(1, 'inch') == 0.0254

    def test_feet(self):
        """
        Test conversion from feet to meters.
        1 foot should equal exactly 0.3048 meters.
        """
        assert convert_to_meters(1, 'ft') == 0.3048

    def test_yards(self):
        """
        Test conversion from yards to meters.
        1 yard should equal exactly 0.9144 meters.
        """
        assert convert_to_meters(1, 'yd') == 0.9144

    def test_miles(self):
        """
        Test conversion from miles to meters.
        1 mile should equal exactly 1609.344 meters.
        """
        assert convert_to_meters(1, 'mile') == 1609.344

    def test_invalid_unit(self):
        """
        Test that an invalid unit raises a ValueError.
        Passing an unknown unit should raise an exception.
        """
        with pytest.raises(ValueError):
            convert_to_meters(1, 'unknown_unit')

class TestImportCsv:
    """
    Unit tests for the import_csv function.
    """

    def test_valid_gps_csv(self):
        """
        Test that a valid GPS CSV file is successfully imported into a
        DataFrame.
        """
        # Path to the valid GPS CSV file
        csv_file_path = '../data/test/valid_gps.csv'

        # Call the function and check the returned DataFrame
        df = import_csv(csv_file_path)

        # Expected DataFrame
        expected_df = pd.DataFrame({
            'Timestamp': [
                '2024-10-22T08:00:00Z', '2024-10-22T08:01:00Z', '2024-10-22T08:02:00Z',
                '2024-10-22T08:03:00Z', '2024-10-22T08:04:00Z'
            ],
            'Latitude': [40.7128, 34.0522, 51.5074, 48.8566, -33.8688],
            'Longitude': [-74.0060, -118.2437, -0.1278, 2.3522, 151.2093],
            'Altitude': [10, 15, 5, 35, 50]
        })

        # Assert that the DataFrame is as expected
        pd.testing.assert_frame_equal(df, expected_df)

    def test_valid_accelerometer_csv(self):
        """
        Test that a valid accelerometer CSV file is successfully imported into
        a DataFrame.
        """
        # Path to the valid accelerometer CSV file
        csv_file_path = '../data/test/valid_accel.csv'

        # Call the function and check the returned DataFrame
        df = import_csv(csv_file_path)

        # Expected DataFrame
        expected_df = pd.DataFrame({
            'Timestamp': [
                '2024-10-22T08:00:00Z', '2024-10-22T08:01:00Z', '2024-10-22T08:02:00Z',
                '2024-10-22T08:03:00Z', '2024-10-22T08:04:00Z'
            ],
            'Accel_X': [0.01, 0.02, 0.00, -0.01, 0.01],
            'Accel_Y': [0.02, 0.01, 0.00, 0.03, -0.02],
            'Accel_Z': [9.81, 9.82, 9.80, 9.79, 9.81]
        })

        # Assert that the DataFrame is as expected
        pd.testing.assert_frame_equal(df, expected_df)

    def test_empty_file(self):
        """
        Test that an empty CSV file returns None.
        """
        # Path to the empty CSV file
        csv_file_path = '../data/test/empty.csv'

        # Call the function
        df = import_csv(csv_file_path)

        # The function should return None for an empty file
        assert df is None

    def test_invalid_csv(self):
        """
        Test that a CSV with invalid format (e.g., a parsing error) is properly
        handled.


        NOTE - Issues with this malformed CSV:
        Row 2: Missing the "Altitude" value.
        Row 3: Has an extra value (an extra column "extra_column") that doesn't
        match the header.
        Row 4: Missing values for both "Longitude" and "Altitude".
        Row 5: The "Timestamp" value is missing.

        """
        # Path to the invalid CSV file
        csv_file_path = '../data/test/invalid.csv'

        # Call the function
        df = import_csv(csv_file_path)

        # The function should return None for a malformed CSV file
        assert df is None

    def test_file_not_found(self):
        """
        Test that a FileNotFoundError is properly handled when the CSV file does not exist.
        """
        # Path to a non-existent CSV file
        csv_file_path = '../data/test/nonexistent.csv'

        # Call the function and expect None
        df = import_csv(csv_file_path)

        # The function should return None for a missing file
        assert df is None

from utils import (
    convert_to_feet, timecode_to_unix, haversine_with_altitude,
    plot_gpstrip_segments, plot_gpstrip_segments_with_color,
    plot_acceltrip_acceleration_with_color, plot_acceltrip_velocity,
    plot_acceltrip_velocity_with_acceleration_color, plot_3d_trajectory,
    render_multiplot
)

class TestConvertToFeet:
    """
    Unit tests for the convert_to_feet function.
    """

    def test_meters_to_feet(self):
        """
        Test conversion from meters to feet.
        1 meter should equal approximately 3.28084 feet.
        """
        assert pytest.approx(convert_to_feet(1, 'm'), 0.0001) == 3.28084

    def test_invalid_unit(self):
        """
        Test that an invalid unit raises a ValueError.
        Passing an unknown unit should raise an exception.
        """
        with pytest.raises(ValueError):
            convert_to_feet(1, 'unknown_unit')


class TestTimecodeToUnix:
    """
    Unit tests for the timecode_to_unix function.
    """

    def test_valid_timecode(self):
        """
        Test conversion of a valid time string to Unix time.
        """
        time_str = '2024-01-01 00:00:00.000 UTC+0000'
        assert timecode_to_unix(time_str) == 1704067200


class TestHaversineWithAltitude:
    """
    Unit tests for the haversine_with_altitude function.
    """

    def test_distance_calculation(self):
        """
        Test calculation of 3D distance between two points with altitude.
        """
        start = {'lat': 40.7128, 'lon': -74.0060, 'alt': 10}
        end = {'lat': 34.0522, 'lon': -118.2437, 'alt': 20}
        distance = haversine_with_altitude(start, end)
        assert pytest.approx(distance, 0.1) == 3940489.2  # Expected distance in meters


class TestPlots:
    """
    Placeholder tests for plot functions in utils.py.
    These tests ensure the functions execute without errors.
    """

    def test_plot_gpstrip_segments(self, mocker):
        """
        Test that plot_gpstrip_segments executes without errors.
        """
        mocker.patch('matplotlib.pyplot.show')
        gps_trip = mocker.Mock()
        gps_trip.segments = mocker.Mock(columns=['start_long', 'start_lat', 'end_long', 'end_lat'])
        plot_gpstrip_segments(gps_trip)

    def test_plot_gpstrip_segments_with_color(self, mocker):
        """
        Test that plot_gpstrip_segments_with_color executes without errors.
        """
        mocker.patch('matplotlib.pyplot.show')
        gps_trip = mocker.Mock()
        gps_trip.segments = mocker.Mock(columns=['start_long', 'start_lat', 'end_long', 'end_lat', 'start_t', 'stop_t'])
        plot_gpstrip_segments_with_color(gps_trip)

    def test_plot_acceltrip_acceleration_with_color(self, mocker):
        """
        Test that plot_acceltrip_acceleration_with_color executes without errors.
        """
        mocker.patch('matplotlib.pyplot.show')
        accel_trip = mocker.Mock()
        accel_trip.segments = mocker.Mock(columns=['start_t', 'total_acceleration'])
        plot_acceltrip_acceleration_with_color(accel_trip)

    def test_plot_acceltrip_velocity(self, mocker):
        """
        Test that plot_acceltrip_velocity executes without errors.
        """
        mocker.patch('matplotlib.pyplot.show')
        accel_trip = mocker.Mock()
        accel_trip.segments = mocker.Mock(columns=['start_t', 'velocity_z'])
        plot_acceltrip_velocity(accel_trip)

    def test_plot_3d_trajectory(self, mocker):
        """
        Test that plot_3d_trajectory executes without errors.
        """
        mocker.patch('matplotlib.pyplot.show')
        accel_trip = mocker.Mock()
        accel_trip.segments = mocker.Mock(columns=['start_t', 'velocity_x', 'velocity_y', 'velocity_z'])
        plot_3d_trajectory(accel_trip)


class TestRenderMultiplot:
    """
    Unit test for the render_multiplot function.
    """

    def test_render_multiplot_executes(self, mocker):
        """
        Test that render_multiplot executes without errors.
        """
        mocker.patch('matplotlib.pyplot.savefig')
        list1 = [lambda ax: ax.plot([0, 1], [0, 1])]
        list2 = [lambda ax: ax.plot([1, 0], [1, 0])]
        render_multiplot(list1, list2)
