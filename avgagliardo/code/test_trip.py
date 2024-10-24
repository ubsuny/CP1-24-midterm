"""
test_trip.py

This module contains unit tests for the TripBase class defined in the trip module.
The tests validate the proper import of trip data and metadata from CSV files,
correct extraction of trip times (start, stop, and duration), and exception handling
for CSV import errors.

Module Dependencies:
    pytest, pandas
"""

import pytest
import pandas as pd
from trip import TripBase, GpsTrip, AccelTrip
from trip import CSVImportError




class TestTripBase:
    """
    Test class for the TripBase class from the trip module.
    Contains unit tests that check the functionality of the TripBase class,
    including data import, metadata processing, and error handling.
    """

    @pytest.fixture
    def mock_import_csv(self, monkeypatch):
        """
        Fixture that mocks the `import_csv` function to return predefined DataFrames
        for testing purposes. Mocks the import function for both trip data and metadata.

        Args:
            monkeypatch: pytest fixture to replace the import_csv function.
        """
        def mock_import(path):
            if 'meta' in path:
                # Return a mock metadata DataFrame
                return pd.DataFrame({
                    'event': ['START', 'PAUSE'],
                    'system time': [1000, 2000],
                    'system time text': ['2024-10-20 10:00:00', '2024-10-20 12:00:00']
                })
            # Return a mock raw data DataFrame
            return pd.DataFrame({
                'col1': [1, 2],
                'col2': [3, 4]
            })
        monkeypatch.setattr('trip.import_csv', mock_import)

    def test_tripbase_initialization(self, mock_import_csv):
        """
        Test the initialization of the TripBase class. This test checks whether
        the raw trip data and metadata are correctly imported from CSV files
        and verifies that trip times (start, stop, and duration) are properly extracted.

        Asserts:
            - The raw trip data is imported as a non-empty DataFrame.
            - The metadata is imported as a non-empty DataFrame.
            - The start and stop times (Unix and UTC formats) are extracted correctly.
            - The trip duration is calculated accurately.
        """
        trip = TripBase('test_trip')
        print(type(mock_import_csv))
        # Check if the raw data is correctly imported
        raw_frame = trip.get_raw_frame()
        assert isinstance(raw_frame, pd.DataFrame)
        assert not raw_frame.empty

        # Check if metadata is correctly imported and processed
        raw_meta = trip.get_raw_frame_meta()
        assert isinstance(raw_meta, pd.DataFrame)
        assert not raw_meta.empty

        # Test if times were correctly extracted
        assert trip.times['start_time_unix'] == 1000
        assert trip.times['stop_time_unix'] == 2000
        assert trip.times['duration'] == 1000

    def test_tripbase_csv_import_error(self, monkeypatch):
        """
        Test that verifies the proper handling of CSV import errors in TripBase.
        This test ensures that the custom CSVImportError exception is raised when
        importing CSV data fails (i.e., when the imported data is `None`).

        Args:
            monkeypatch: pytest fixture to mock a failed CSV import.

        Asserts:
            - The CSVImportError is raised when CSV import fails.
        """
        def mock_import_fail(_):
            return None  # Simulate a failed CSV import
        monkeypatch.setattr('trip.import_csv', mock_import_fail)

        # Ensure that CSVImportError is raised when import_csv returns None
        with pytest.raises(CSVImportError):
            TripBase('test_trip')

class TestGpsTrip:
    """
    Test class for the GpsTrip class from the trip module.
    Contains unit tests that check the functionality of the GpsTrip class.
    """

    @pytest.fixture
    def mock_import_csv(self, monkeypatch):
        """
        Fixture that mocks the `import_csv` function to return predefined DataFrames
        for testing purposes. Mocks the import function for both GPS trip data and metadata.

        Args:
            monkeypatch: pytest fixture to replace the import_csv function.
        """
        def mock_import(path):
            if 'meta' in path:
                # Return a mock metadata DataFrame
                return pd.DataFrame({
                    'event': ['START', 'PAUSE'],
                    'system time': [1000, 2000],
                    'system time text': ['2024-10-20 10:00:00', '2024-10-20 12:00:00']
                })
            # Return a mock GPS data DataFrame
            return pd.DataFrame({
                'Time (s)': [1, 2],
                'Latitude (°)': [40.7128, 40.7138],
                'Longitude (°)': [-74.0060, -74.0050],
                'Altitude (m)': [10, 20],
                'Altitude WGS84 (m)': [11, 21]
            })
        monkeypatch.setattr('trip.import_csv', mock_import)

    def test_gpstrip_initialization(self, mock_import_csv):
        """
        Test the initialization of the GpsTrip class. This test checks whether
        GPS-specific data is correctly imported and processed.

        Asserts:
            - The GPS data is imported as a non-empty DataFrame.
        """
        trip = GpsTrip('test_trip')
        print(mock_import_csv)
        assert isinstance(trip, GpsTrip)
        # Check if the GPS data is correctly imported
        gps_data = trip.data
        assert isinstance(gps_data, pd.DataFrame)
        assert not gps_data.empty

    def test_gpstrip_calculate_segments(self, mock_import_csv):
        """
        Test the calculation of segments for GpsTrip.
        This checks whether the segmentation of GPS data (including distance calculations)
        is done correctly.

        Asserts:
            - The segments DataFrame is correctly calculated and is non-empty.
        """
        trip = GpsTrip('test_trip')
        print(mock_import_csv)
        segments = trip.segments
        assert isinstance(segments, pd.DataFrame)
        assert not segments.empty

class TestAccelTrip:
    """
    Test class for the AccelTrip class from the trip module.
    Contains unit tests that check the functionality of the AccelTrip class.
    """

    @pytest.fixture
    def mock_import_csv(self, monkeypatch):
        """
        Fixture that mocks the `import_csv` function to return predefined DataFrames
        for testing purposes. Mocks the import function for both accelerometer
        trip data and metadata.

        Args:
            monkeypatch: pytest fixture to replace the import_csv function.
        """
        def mock_import(path):
            if 'meta' in path:
                # Return a mock metadata DataFrame
                return pd.DataFrame({
                    'event': ['START', 'PAUSE'],
                    'system time': [1000, 2000],
                    'system time text': ['2024-10-20 10:00:00', '2024-10-20 12:00:00']
                })
            # Return a mock accelerometer data DataFrame (stub for now)
            return pd.DataFrame({
                'Time (s)': [1, 2],
                'X (m/s^2)': [0.1, 0.2],
                'Y (m/s^2)': [0.3, 0.4],
                'Z (m/s^2)': [0.5, 0.6]
            })
        monkeypatch.setattr('trip.import_csv', mock_import)

    def test_acceltrip_initialization(self, mock_import_csv):
        """
        Test the initialization of the AccelTrip class. This test checks whether
        accelerometer-specific data is correctly imported and processed.

        Asserts:
            - The accelerometer data is imported as a non-empty DataFrame.
        """
        trip = AccelTrip('test_trip')
        print(mock_import_csv)
        # Check if the accelerometer data is correctly imported
        accel_data = trip.data
        assert accel_data is None  # Stubbed out, so accel_data should be None for now

    def test_acceltrip_calculate_segments(self, mock_import_csv):
        """
        Test the calculation of segments for AccelTrip.
        This checks whether the segmentation of accelerometer data is stubbed out correctly.

        Asserts:
            - The segments DataFrame is not calculated (since it's a stub).
        """
        trip = AccelTrip('test_trip')
        print(mock_import_csv)
        segments = trip.calculate_segments()
        assert segments is None  # Segments are not yet implemented, so should be None
