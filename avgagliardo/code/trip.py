"""
trip.py

This module defines the TripBase class, which serves as a foundational class for handling trip data.
The class is designed to import trip-related CSV files and metadata, extract important information
such as start/stop times, and calculate the duration of trips.

Classes:
    TripBase: A base class that handles the import and processing of trip data and metadata.
              It includes methods to retrieve raw trip data and metadata, as well as functionality
              to extract time-related details (e.g., start/stop times in Unix and UTC formats).

Functions:
    _import_metadata: Imports metadata from a CSV file and extracts trip timing information.
    _get_raw_frame: Retrieves the raw trip data (stored in a private variable).
    _get_raw_frame_meta: Retrieves the metadata (stored in a private variable).

Exceptions:
    CSVImportError: Custom exception raised when an error occurs during CSV import.
"""

import pandas as pd
import numpy as np

from utils import import_csv, CSVImportError
from utils import haversine_with_altitude as haversine

class TripBase:
    """
    A base class that imports a CSV and stores it in a private variable `raw_frame`
    and metadata in `raw_frame_meta`. It also extracts metadata such as start/stop
    times and calculates the trip duration.

    This class is not meant to be used directly. Instead you should use either
    the GpsTrip or AccelTrip classes.
    """
    def __init__(self, csv_name):
        """
        Initializes the TripBase class by importing trip data and metadata from
        CSV files.

        Args:
            csv_name (str): Name of the CSV file (without extension) that contains trip data.
        """
        # Ensure that the directory path ends with a slash
        if not csv_name.endswith('/'):
            csv_dir = '../data/' + csv_name + '/'  # Directory path
        else:
            csv_dir = '../data/' + csv_name        # Directory path

        # Prepare the csv paths
        csv_path = csv_dir + csv_name + '.csv'                 # Filename
        csv_meta_path = csv_dir + '/meta/time.csv'  # Meta name

        # initilize the times dict
        self.times = {
            "start_time_unix": None,
            "stop_time_unix": None,
            "start_time_utc": None,
            "stop_time_utc": None,
            "duration": None,
        }

        # Initialize the raw and meta data frames as private members
        print("Importing data from: " + csv_path)
        self.__csv_path = csv_path
        print("Importing meta from: " + csv_dir + "meta/time.csv" )
        self.__csv_meta_path = csv_meta_path

        # Import and store the raw data and metadata
        self.__raw_frame = import_csv(self.__csv_path)
        self.__raw_frame_meta = self.import_metadata(self.__csv_meta_path)

        # Define a prefix for labels
        self.trip_type = "BASE"

        # # Define the member for the subclassed data frames and trip segments
        # self.data = None
        # self.segments = None

    def get_raw_frame(self):
        """
        Protected method to access the private raw_frame. This can be accessed
        by child objects to extract data relevant to their context.

        Returns:
            DataFrame: The trip data stored in the private variable
            `__raw_frame`.
        """
        return self.__raw_frame

    def get_raw_frame_meta(self):
        """
        Protected method to access the private raw_frame_meta. This can be
        accessed
        by child objects to extract metadata relevant to their context.

        Returns:
            DataFrame: The metadata stored in the private variable
            `__raw_frame_meta`.
        """
        return self.__raw_frame_meta

    def import_metadata(self, meta_csv_path):
        """
        Imports metadata CSV and extracts start and stop times in Unix and UTC
        formats.
        Stores the duration of the experiment as well.

        Args:
            meta_csv_path (str): Path to the metadata CSV file.

        Returns:
            DataFrame: The metadata DataFrame stored in the private variable
            `__raw_frame_meta`.
        """
        try:
            meta_df = import_csv(meta_csv_path)

            if meta_df is not None:
                # Extract start and stop times from the metadata
                start_event = meta_df[meta_df['event'] == 'START'].iloc[0]
                stop_event = meta_df[meta_df['event'] == 'PAUSE'].iloc[0]

                # Extract Unix and human-readable times from the CSV
                self.times['start_time_unix'] = start_event['system time']
                self.times['stop_time_unix'] = stop_event['system time']
                self.times['start_time_utc'] = start_event['system time text']
                self.times['stop_time_utc'] = stop_event['system time text']

                # Calculate the duration in seconds
                dur = self.times['stop_time_unix'] - self.times['start_time_unix']
                self.times['duration'] = dur
            else:
                # create an error message
                msg = f"Failed to import metadata from" \
                      f"{meta_csv_path}. DataFrame is None."
                # raise the exception with the details in msg
                raise CSVImportError(msg)

            return meta_df

        except Exception as e:
            msg = "An error occurred while importing the" \
                  f" metadata CSV: {str(e)}"
            raise CSVImportError(msg) from e

    def report_trip_summary(self):
        """
        Public method that generates a summary report of the trip details.
        It reports the trip type, start time in UTC, trip duration, and the
        number of frames in the raw trip data.

        Returns:
            str: A formatted string containing the trip type, start time (UTC),
            duration (in seconds), and the number of data frames.
        """
        trip_type = self.trip_type
        start_time_utc = self.times['start_time_utc'] if self.times['start_time_utc'] else 'Unknown'
        duration = self.times['duration'] if self.times['duration'] is not None else 'Unknown'
        num_frames = len(self.__raw_frame) if self.__raw_frame is not None else 0

        return(
            f"Trip Summary:\n"
            f"Type of trip: {trip_type}\n"
            f"Start time (UTC): {start_time_utc}\n"
            f"Duration: {duration} seconds\n"
            f"Number of frames: {num_frames}"
        )

class GpsTrip(TripBase):
    """
    A class that inherits from TripBase, specifically for trips that include GPS data.
    This class adds functionality to handle GPS coordinates and other related metadata.

    Attributes:
        trip_type (str): The type of the trip, overridden to be 'GPS' for this class.
        data (DataFrame): A DataFrame holding specific GPS data (Time, Latitude,
        Longitude, Altitude, Altitude WGS84).
    """
    def __init__(self, csv_name):
        """
        Initializes the GpsTrip class by calling the base class initializer to handle
        trip data and metadata import. Additionally, it loads GPS-specific data.

        Args:
            csv_name (str): Name of the CSV file (without extension) that contains trip data.
        """
        # Call the base class initializer
        super().__init__(csv_name)

        # Set the trip_type to "GPS" for this specific trip
        self.trip_type = "GPS"

        # Extract GPS-specific data and store in self.data
        self.data = self.extract_gps_data()
        self.segments = self.calculate_segments()

    def extract_gps_data(self):
        """
        Extracts specific GPS data columns from the raw trip data, including:
        "Time (s)", "Latitude (°)", "Longitude (°)", "Altitude (m)",
        "Altitude WGS84 (m)".

        If any of the required columns are missing, it prints an error message.

        Returns:
            DataFrame: A DataFrame containing GPS data if all required columns
            are present, otherwise returns None.
        """
        required_columns = [
            "Time (s)",
            "Latitude (°)",
            "Longitude (°)",
            "Altitude (m)",
            "Altitude WGS84 (m)"
        ]

        # Check if the raw frame has been loaded
        rf = self.get_raw_frame()
        if rf is not None:
            # Check if all required columns are present in the raw data
            if all(col in rf.columns for col in required_columns):
                # Extract the required columns and store them in a new DataFrame
                gps_data = rf[required_columns]
                return gps_data

            missing_cols = [col for col in required_columns if col not in rf.columns]
            print(f"Error: Missing GPS columns in the raw data: {missing_cols}")
        else:
            print("Error: Raw frame is empty.")

        # Return None if extraction failed
        return None

    def calculate_segments(self):
        """
        Takes a DataFrame with 'Latitude (°)', 'Longitude (°)', and 'Altitude (m)' columns
        and calculates the Euclidean distance, Haversine distance, and 3D distance between
        each pair of sequential GPS points. Stores the start point, end point, and distances
        in a new DataFrame called 'segments'.

        Returns:
            DataFrame: A DataFrame containing the start point, end point, and calculated distances.
        """
        # Get the dataframe and make a copy
        df = self.data.copy()

        # Shift latitude, longitude, and altitude to get the next point's coordinates
        df['Latitude_next'] = df['Latitude (°)'].shift(-1)
        df['Longitude_next'] = df['Longitude (°)'].shift(-1)
        df['Altitude_next'] = df['Altitude (m)'].shift(-1)

        # Drop the last row, as it will have NaN values due to shifting
        df = df.dropna(subset=['Latitude_next', 'Longitude_next', 'Altitude_next'])


        # Calculate Latitude and Longitude displacements
        df['Latitude_Displacement'] = df['Latitude_next'] - df['Latitude (°)']
        df['Longitude_Displacement'] = df['Longitude_next'] - df['Longitude (°)']

        # Calculate the Euclidean distance between each pair of points (ignoring
        # altitude for now)
        df['Degree_Distance'] = np.sqrt(
            (df['Latitude_next'] - df['Latitude (°)'])**2 +
            (df['Longitude_next'] - df['Longitude (°)'])**2
        )

        # Convert latitude and longitude displacements to meters
        # Latitude displacement in meters
        df['Latitude_Displacement_m'] = df['Latitude_Displacement'] * 111320
        # Longitude displacement in meters
        df['Longitude_Displacement_m'] = (df['Longitude_Displacement'] * 111320
            * np.cos(np.radians(df['Latitude (°)'])))


        # Calculate the planar distance in meters
        df['Planar_Distance'] = np.sqrt(df['Latitude_Displacement_m']**2 +
            df['Longitude_Displacement_m']**2)

        # Calculate the 3D curved distance (Haversine + Altitude difference)
        df['Curved_Distance'] = haversine(
            df['Latitude (°)'], df['Longitude (°)'],
            df['Latitude_next'], df['Longitude_next'],
            df['Altitude (m)'], df['Altitude_next']
        )

        # Create the segments DataFrame with start point, end point, planar
        # distance, and curved distance
        segments = pd.DataFrame({
            'Start_Latitude (°)': df['Latitude (°)'],
            'Start_Longitude (°)': df['Longitude (°)'],
            'Start_Altitude (m)': df['Altitude (m)'],
            'End_Latitude (°)': df['Latitude_next'],
            'End_Longitude (°)': df['Longitude_next'],
            'End_Altitude (m)': df['Altitude_next'],
            # Displacement for Latitude
            'Latitude_Displacement (°)': df['Latitude_Displacement'],
            # Displacement for Longitude
            'Longitude_Displacement (°)': df['Longitude_Displacement'],
            # Euclidean distance in degrees
            'Degree_Distance (°)': df['Degree_Distance'],
            # Planar distance in meters
            'Planar_Distance (m)': df['Planar_Distance'],
            # 3D distance in meters
            'Curved_Distance (m)': df['Curved_Distance']
        })

        return segments

class AccelTrip(TripBase):
    """
    A class that inherits from TripBase, specifically for trips that include
    accelerometer data.

    This class stubs out methods that will eventually handle accelerometer-
    specific data.

    Attributes:
        trip_type (str): The type of the trip, overridden to be 'ACCEL' for
        this class.
        data (DataFrame): A DataFrame holding specific accelerometer data (e.g.,
        time, x, y, z axes).
    """

    def __init__(self, csv_name):
        """
        Initializes the AccelTrip class by calling the base class initializer
        to handle
        trip data and metadata import. Additionally, it will eventually handle
        accelerometer-specific data.

        Args:
            csv_name (str): Name of the CSV file (without extension) that
            contains trip data.
        """
        # Call the base class initializer
        super().__init__(csv_name)

        # Set the trip_type to "ACCEL" for this specific trip
        self.trip_type = "ACCEL"

        # Stub out the accelerometer data for now
        self.data = self.extract_accel_data()
        self.segments = None

    def extract_accel_data(self):
        """
        Extracts accelerometer data from the raw trip data, including:
        - Time (s)
        - Linear Acceleration x (m/s^2)
        - Linear Acceleration y (m/s^2)
        - Linear Acceleration z (m/s^2)
        - Absolute acceleration (m/s^2)

        The columns are renamed to more convenient names for processing:
        - Time (s) → time
        - Linear Acceleration x (m/s^2) → accel_x
        - Linear Acceleration y (m/s^2) → accel_y
        - Linear Acceleration z (m/s^2) → accel_z
        - Absolute acceleration (m/s^2) → accel_absolute

        Returns:
            DataFrame: A DataFrame containing the renamed accelerometer
            data columns.
        """
        # Check if the raw frame exists
        raw_frame = self.get_raw_frame()
        if raw_frame is not None:
            required_columns = [
                "Time (s)",
                "Linear Acceleration x (m/s^2)",
                "Linear Acceleration y (m/s^2)",
                "Linear Acceleration z (m/s^2)",
                "Absolute acceleration (m/s^2)"
            ]

            # Check if the required columns are present
            if all(col in raw_frame.columns for col in required_columns):
                # Extract and rename the relevant columns
                accel_data = raw_frame[required_columns].rename(columns={
                    "Time (s)": "time",
                    "Linear Acceleration x (m/s^2)": "accel_x",
                    "Linear Acceleration y (m/s^2)": "accel_y",
                    "Linear Acceleration z (m/s^2)": "accel_z",
                    "Absolute acceleration (m/s^2)": "accel_absolute"
                })
                return accel_data
            else:
                missing_cols = [col for col in required_columns if col not in raw_frame.columns]
                print(f"Error: Missing accelerometer columns in the raw data: {missing_cols}")
                return None
        else:
            print("Error: Raw frame is empty.")
            return None

    def calculate_segments(self):
        """
        Stub method to calculate segments based on accelerometer data.
        This method will be implemented later.

        Returns:
            None: For now, this method is a stub.
        """
        print("Stub: calculate_segments will be implemented later.")
        return None

    def report_trip_summary(self):
        """
        Overrides the report_trip_summary method to include accelerometer-
        specific details.
        Currently stubs out the implementation.

        Returns:
            str: A formatted string containing the trip type and stub message.
        """
        base_summary = super().report_trip_summary()
        accel_status = "Not yet available (stub method)"

        return (
            f"{base_summary}\n"
            f"Accelerometer Data: {accel_status}"
        )
