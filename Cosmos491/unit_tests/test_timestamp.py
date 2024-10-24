import pytest
import pandas as pd
import numpy as np
from datetime import datetime
from code.convert_unix_time import add_timestamp_to_data, process_multiple_files  # Ensure correct module import

# Mock data for the CSV files using pandas DataFrame
mock_data = pd.DataFrame({
    'Time (s)': [0, 1, 2, 3],
    'Acceleration_x': [0.17, 0.18, 0.20, 0.19],
    'Acceleration_y': [0.15, 0.16, 0.17, 0.18],
    'Acceleration_z': [0.00, 0.01, 0.02, 0.01]
})

def test_add_timestamp_to_data():
    # Save mock_data to a temporary CSV file for testing
    mock_file = 'mock_data.csv'
    mock_data.to_csv(mock_file, index=False)

    # Expected start time for the test
    start_time_str = "2024-10-23 17:16:00"

    # Read the mock CSV and apply the timestamp logic
    df_with_timestamps = add_timestamp_to_data(mock_file, start_time_str)

    # Manually calculate expected timestamp and Unix time
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    expected_timestamps = [
        start_time,
        start_time + pd.Timedelta(seconds=1),
        start_time + pd.Timedelta(seconds=2),
        start_time + pd.Timedelta(seconds=3)
    ]
    expected_unix_times = [int(ts.timestamp()) for ts in expected_timestamps]

    # Verify that the timestamps are correctly calculated
    assert np.all(df_with_timestamps['timestamp'].values == expected_timestamps)
    assert np.all(df_with_timestamps['unix_time'].values == expected_unix_times)

def test_process_multiple_files():
    # Mocking multiple CSV files with pandas DataFrame
    mock_file_1 = 'mock_data_1.csv'
    mock_file_2 = 'mock_data_2.csv'
    mock_data.to_csv(mock_file_1, index=False)
    mock_data.to_csv(mock_file_2, index=False)

    # Mock file paths and start times
    file_paths = [mock_file_1, mock_file_2]
    start_times = [
        "2024-10-23 17:16:00",
        "2024-10-23 17:12:00"
    ]

    # Process the mock data
    data_frames = process_multiple_files(file_paths, start_times)

    # Verify that timestamps and Unix times are added for both datasets
    for i, start_time_str in enumerate(start_times):
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
        expected_timestamps = [
            start_time,
            start_time + pd.Timedelta(seconds=1),
            start_time + pd.Timedelta(seconds=2),
            start_time + pd.Timedelta(seconds=3)
        ]
        expected_unix_times = [int(ts.timestamp()) for ts in expected_timestamps]

        df_with_timestamps = data_frames[file_paths[i]]

        # Verify timestamps and Unix time for each row in both datasets
        assert np.all(df_with_timestamps['timestamp'].values == expected_timestamps)
        assert np.all(df_with_timestamps['unix_time'].values == expected_unix_times)
