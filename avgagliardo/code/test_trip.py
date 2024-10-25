"""
test_trip.py

Tests the different classes in trip.py
"""

from unittest.mock import patch
import pytest
import pandas as pd
from trip import TripBase, CSVImportError

# Mock data for the DataFrames
mock_raw_frame = pd.DataFrame({"Column1": [1, 2, 3], "Column2": [4, 5, 6]})
mock_meta_frame = pd.DataFrame(
    {"event": ["START", "PAUSE"],
    "system time text": ["2023-01-01 00:00:00.000 UTC+0000",
    "2023-01-01 01:00:00.000 UTC+0000"]}
)

@patch("utils.import_csv", side_effect=[mock_raw_frame, mock_meta_frame])
def test_tripbase_initialization(mock_import_csv):
    """Test that TripBase initializes with the correct experiment name."""
    print(mock_import_csv)
    trip = TripBase("AVG001_gps_circle_walk_1")
    n = "AVG001_gps_circle_walk_1"
    m = "Experiment name should match the initialized value."
    assert trip.experiment_name == n, m

@patch("utils.import_csv", side_effect=[mock_raw_frame, mock_meta_frame])
def test_tripbase_get_raw_frame(mock_import_csv):
    """Test that get_raw_frame method returns a DataFrame."""
    print(mock_import_csv)
    trip = TripBase("AVG001_gps_circle_walk_1")
    raw_frame = trip.get_raw_frame()
    assert raw_frame is not None, "Raw frame should not be None."
    assert isinstance(raw_frame, pd.DataFrame), "Raw frame should be a DataFrame."

@patch("utils.import_csv", side_effect=[mock_raw_frame, mock_meta_frame])
def test_tripbase_get_raw_frame_meta(mock_import_csv):
    """Test that get_raw_frame_meta method returns a DataFrame."""
    print(mock_import_csv)
    trip = TripBase("AVG001_gps_circle_walk_1")
    raw_frame_meta = trip.get_raw_frame_meta()
    assert raw_frame_meta is not None, "Raw frame meta should not be None."
    assert isinstance(raw_frame_meta, pd.DataFrame), "Raw frame meta should be a DataFrame."

@patch("utils.import_csv", side_effect=[mock_raw_frame, mock_meta_frame])
def test_tripbase_report_trip_summary(mock_import_csv):
    """Test that report_trip_summary returns a formatted string."""
    print(mock_import_csv)
    trip = TripBase("AVG001_gps_circle_walk_1")
    summary = trip.report_trip_summary()
    assert isinstance(summary, str), "Report summary should be a string."
    assert "Trip Summary" in summary, "Summary should contain 'Trip Summary'."

@patch("utils.import_csv", side_effect=Exception("File not found"))
def test_tripbase_import_metadata_invalid_path(mock_import_csv):
    """Test that import_metadata raises an error with an invalid path."""
    print(mock_import_csv)
    trip = TripBase("AVG001_gps_circle_walk_1")
    with pytest.raises(CSVImportError):
        trip.import_metadata("invalid_path.csv")
