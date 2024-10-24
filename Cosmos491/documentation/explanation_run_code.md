# Project Documentation

This project contains multiple Python functions for data processing and analysis. The functions include unit conversions, calculating the Haversine distance between two points on Earth, determining the direction of motion based on acceleration data, and adding timestamps to CSV files with acceleration data.

## Prerequisites
Before running the code, ensure you have the following Python libraries installed:
- **pandas**
- **numpy**
- **matplotlib**
- **pytest** (for running unit tests)
- **pylint** (for linting the code)

You can install the necessary libraries using pip:

## How to Run the Code

### 1. Conversion Functions

Code File conversion.py contains two functions feet_to_meters(feet) which converst a distance feet to meters and yards_to_meters(yards) which converts from yards to meters.

### 2. Haversine function 
distance_gps_location.py file contains the haversine(lat1, lon1, lat2, lon2) function, which calculates the great-circle distance between two points on Earth using their latitude and longitude.

### 3. calculate_direction(acceleration_data) function
Code File: direction_calculations.py  file contains the calculate_direction(acceleration_data) function, which calculates the direction of motion based on acceleration data in the x, y, and z axes.

### 4. Timestamp and Unix Time Processing for CSV Files
Code File: timestamp_processing.py contains two functions:
- add_timestamp_to_data(file_path, start_time_str): Adds a timestamp and Unix time to a CSV file containing time and acceleration data.
- process_multiple_files(file_paths, start_times): Processes multiple CSV files and adds timestamps and Unix times.

### 5. Unit tests
You can run unit tests to ensure that all functions are working correctly. The tests are located in separate files:
- test_conversion.py
- test_haversine.py
- test_calculate_direction.py
- test_timestamp.py

## Summary
- Conversion functions: Converts feet/yards to meters.
- Haversine function: Calculates the great-circle distance between two points.
- Direction function: Computes direction of motion from acceleration data.
- Timestamp processing: Adds timestamps and Unix time to CSV files.
- Unit tests: Run tests using pytest.
