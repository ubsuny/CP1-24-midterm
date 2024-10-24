"""
This module contains utility functions that do not belong as first order
members of the Trip class.

List out classes and functions:...

"""
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

class CSVImportError(Exception):
    """
    Custom exception raised when a CSV file cannot be imported.
    Provides an error message with details about the failure.
    """
    def __init__(self, message):
        super().__init__(message)

def convert_to_meters(value, unit):
    """
    Converts a given value from a specified unit to meters. This function
    uses exact quantities for conversion factors exclusively.

    Args:
        value (number): The numerical value to be converted.
        unit (str): The unit of the value to convert from. Supported units
        include:
                    'km' (kilometers), 'cm' (centimeters), 'mm' (millimeters),
                    'inch' (inches), 'ft' (feet), 'yd' (yards), 'mile' (miles).

    Returns:
        Number: The equivalent value in meters (a float).

    Raises:
        ValueError: If the specified unit is not supported.
    """
    # Let's store the unit coverstion factors neatly within in a dict.
    conversion_factors = {
        'km': 1000.0,          # Kilometers to meters (exact quantity)
        'cm': 0.0100,          # Centimeters to meters (exact quantity)
        'mm': 0.0010,         # Millimeters to meters (exact quantity)
        'inch': 0.0254,      # Inches to meters (exact quantity)
        'in': 0.0254,      # Inches to meters (exact quantity)
        'ft': 0.3048,        # Feet to meters (exact quantity)
        'feert': 0.3048,        # Feet to meters (exact quantity)
        'yd': 0.9144,        # Yards to meters (exact quantity)
        'yard': 0.9144,        # Yards to meters (exact quantity)
        'mile': 1609.344,      # Miles to meters (exact quantity)
        'ml': 1609.344      # Miles to meters (exact quantity)
    }

    # Convert the value using the conversion factor for the unit
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        raise ValueError(f"Unknown unit: {unit}")

def import_csv(csv_path):
    """
    Imports data from a CSV file (that uses commas, not semicolons) into a
     pandas DataFrame. It is then returned to the caller.

    Args:
        csv_path (str): The path to the CSV file.

    Returns:
        DataFrame: The data from the CSV file as a pandas DataFrame.
    """
    # Attempt to read in the csv, or throw the proper exception
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_path)
        # Return it to the calling function
        return df

    # If the the file can't be found
    # Throw the exception, print the error, and return None
    except FileNotFoundError as e:
        print(f"Error: The file '{csv_path}' was not found.")
        print(f"Details: {str(e)}")
        return None
    # If the file is empty
    # Throw an exception, print the error, and return None
    except pd.errors.EmptyDataError as e:
        print(f"Error: The file '{csv_path}' is empty.")
        print(f"Details: {str(e)}")
        return None
    # If the file is malformed and cannot be parsed
    # Throw an exception, print the error, and return None
    except pd.errors.ParserError as e:
        print(f"Error: The file '{csv_path}' could not be parsed.")
        print(f"Details: {str(e)}")
        return None

def timecode_to_unix(time_str):
    """
    Converts a time string in the ddefault format 'YYYY-MM-DD HH:MM:SS.sss
    UTC±HH:MM' to Unix time.

    Args:
        time_str (str): A string representing the time with timezone.

    Returns:
        int: Unix timestamp corresponding to the given time.
    """
    # Parse the string into a datetime object with timezone info
    dt_with_tz = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f %Z%z')

    # Convert to Unix timestamp
    unix_time = int(dt_with_tz.timestamp())

    return unix_time

def haversine_with_altitude(lat1, lon1, lat2, lon2, alt1, alt2):
    """
    Calculate the 3D great-circle distance between two points on the spherical
    Earth surface, including the euclidian altitude difference.

    The output distance is in meters.

    Args:
        lat1, lon1, alt1: Latitude, Longitude, and Altitude of point 1.
        lat2, lon2, alt2: Latitude, Longitude, and Altitude of point 2.

    Returns:
        distance (float): The 3D distance between the two points in meters.
    """
    R = 6371.0  # Radius of Earth in kilometers

    # Convert degrees to radians
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    # Differences in latitudes, longitudes, and altitudes
    dlat = lat2 - lat1  # Lat dif in radians
    dlon = lon2 - lon1  # Long dif in radians
    dalt = alt2 - alt1  # Altitude difference in meters

    # Haversine formula for the distance over the Earth's surface (in kilometers)
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    surface_distance_km = R * c  # Distance in kilometers

    # convert curved surface distance from km to meters
    surface_distance_m = surface_distance_km * 1000  # Convert to meters

    # 3D eucldian distance, using altitude
    distance_3d = np.sqrt(surface_distance_m**2 + dalt**2)

    return distance_3d

def plot_gpstrip_segments(gps_trip):
    """
    Plots the segments of a GpsTrip object using longitude as x and latitude as y in a 2D plot.

    Args:
        gps_trip (GpsTrip): A GpsTrip object with segment data containing longitude and latitude.

    Returns:
        None: Displays the plot using Matplotlib.
    """
    if gps_trip.segments is None:
        print("Error: No segment data available to plot.")
        return

    segments = gps_trip.segments

    # Check if necessary columns exist in the segments DataFrame
    if not {'start_long', 'start_lat', 'end_long', 'end_lat'}.issubset(segments.columns):
        print("Error: Missing longitude or latitude data in segments.")
        return

    plt.figure(figsize=(10, 6))

    # Plot each segment
    for index, row in segments.iterrows():
        plt.plot([row['start_long'], row['end_long']],
                 [row['start_lat'], row['end_lat']], 'bo-', label='Segment' if index == 0 else "")

    # Label the axes
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('GPS Trip Segments (Longitude vs Latitude)')

    # Add grid and show plot
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_gpstrip_segments_with_color(gps_trip):
    """
    Plots the segments of a GpsTrip object using longitude as x and latitude as
    y in a 2D plot, with the color of each point corresponding to its relative
    time in the experiment.

    The colors transition from red (start) to purple (end) based on time, just
    like the visible light spectrum!

    Args:
        gps_trip (GpsTrip): A GpsTrip object with segment data containing
        longitude and latitude.

    Returns:
        None: Displays the plot using Matplotlib.
    """
    if gps_trip.segments is None:
        print("Error: No segment data available to plot.")
        return

    segments = gps_trip.segments

    # Check if necessary columns exist in the segments DataFrame
    if not {'start_long', 'start_lat', 'end_long', 'end_lat', 'start_t', 'stop_t'}.issubset(segments.columns):
        print("Error: Missing longitude, latitude, or time data in segments.")
        return

    # Normalize time data to range from 0 to 1 for color mapping
    times = segments['start_t'].values
    norm = plt.Normalize(times.min(), times.max())  # Normalize the time range

    # Create the color map (from red to purple)
    cmap = plt.cm.plasma

    plt.figure(figsize=(10, 6))

    # Plot each segment with color corresponding to its start time
    longitudes = np.concatenate([segments['start_long'].values, segments['end_long'].values])
    latitudes = np.concatenate([segments['start_lat'].values, segments['end_lat'].values])
    colors = np.concatenate([segments['start_t'].values, segments['start_t'].values])  # Use start time for coloring

    # Use scatter to plot points with colors based on the time
    sc = plt.scatter(longitudes, latitudes, c=colors, cmap=cmap, norm=norm, marker='o')

    # Create colorbar to indicate time progression
    cbar = plt.colorbar(sc)
    cbar.set_label('Time (s)')

    # Label the axes
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('GPS Trip Segments with Direction of Travel (Time Progression)')

    # Add grid and show plot
    plt.grid(True)
    plt.show()

def plot_acceltrip_velocity(accel_trip, component='z'):
    """
    Plots the specified velocity component (x, y, or z) of an AccelTrip object over time.

    Args:
        accel_trip (AccelTrip): An AccelTrip object with segment data containing time and velocity components.
        component (str): The velocity component to plot ('x', 'y', or 'z'). Defaults to 'z'.

    Returns:
        None: Displays the plot using Matplotlib.
    """
    if accel_trip.segments is None:
        print("Error: No segment data available to plot.")
        return

    segments = accel_trip.segments

    # Map component to the appropriate column name
    velocity_column = f'velocity_{component}'
    if not {'start_t', velocity_column}.issubset(segments.columns):
        print(f"Error: Missing time or {component}-velocity data in segments.")
        return

    # Extract the time and chosen velocity columns
    times = segments['start_t']
    velocity = segments[velocity_column]

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(times, velocity, 'bo-', label=f'{component.upper()}-Velocity')

    # Label the axes
    plt.xlabel('Time (s)')
    plt.ylabel(f'{component.upper()}-Velocity (m/s)')
    plt.title(f'{component.upper()}-Velocity over Time for AccelTrip')

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

def plot_acceltrip_velocity_with_acceleration_color(accel_trip, component='z', compression_factor=1.0):
    """
    Plots the specified velocity component (x, y, or z) of an AccelTrip object over time, with color representing
    the direction of acceleration. Red indicates positive acceleration, and purple indicates negative acceleration.

    A compression factor is applied to the acceleration values to control the color spectrum, making a wider range
    of colors visible (compressing the center dominance).

    Args:
        accel_trip (AccelTrip): An AccelTrip object with segment data containing time and velocity components.
        component (str): The velocity component to plot ('x', 'y', or 'z'). Defaults to 'z'.
        compression_factor (float): Factor to compress the center of the color spectrum. Defaults to 1.0.

    Returns:
        None: Displays the plot using Matplotlib.
    """
    if accel_trip.segments is None:
        print("Error: No segment data available to plot.")
        return

    segments = accel_trip.segments

    # Map component to the appropriate column name
    velocity_column = f'velocity_{component}'
    if not {'start_t', velocity_column}.issubset(segments.columns):
        print(f"Error: Missing time or {component}-velocity data in segments.")
        return

    # Extract the time and chosen velocity columns
    times = segments['start_t'].values
    velocity = segments[velocity_column].values

    # Calculate the change in velocity (acceleration) between consecutive points
    acceleration = np.diff(velocity, prepend=velocity[0])

    # Apply compression to the acceleration values to broaden the color spectrum
    compressed_acceleration = np.sign(acceleration) * (np.abs(acceleration) ** (1 / compression_factor))

    # Normalize the compressed acceleration values for color mapping
    norm = plt.Normalize(compressed_acceleration.min(), compressed_acceleration.max())

    # Create the color map (from purple to red)
    cmap = plt.cm.nipy_spectral

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Use scatter to plot points with colors based on the compressed acceleration direction
    sc = plt.scatter(times, velocity, c=compressed_acceleration, cmap=cmap, norm=norm, marker='o')

    # Create colorbar to indicate acceleration direction
    cbar = plt.colorbar(sc)
    cbar.set_label(f'Scaled Acceleration (m/s²)')

    # Label the axes
    plt.xlabel('Time (s)')
    plt.ylabel(f'{component.upper()}-Velocity (m/s)')
    plt.title(f'{component.upper()}-Velocity over Time for AccelTrip (Colored by Acceleration Direction)')

    # Add grid
    plt.grid(True)

    # Show the plot
    plt.show()

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_trajectory(accel_trip):
    """
    Plots the 3D trajectory of an AccelTrip object using cumulative sums of the velocity components to approximate position.
    The color of the trajectory represents the time progression.

    Args:
        accel_trip (AccelTrip): An AccelTrip object with segment data containing velocity components.

    Returns:
        None: Displays the 3D plot using Matplotlib.
    """
    if accel_trip.segments is None:
        print("Error: No segment data available to plot.")
        return

    segments = accel_trip.segments

    # Check if the necessary columns exist in the segments DataFrame
    if not {'start_t', 'velocity_x', 'velocity_y', 'velocity_z'}.issubset(segments.columns):
        print("Error: Missing velocity or time data in segments.")
        return

    # Extract time and velocity components
    times = segments['start_t'].values
    velocity_x = segments['velocity_x'].values
    velocity_y = segments['velocity_y'].values
    velocity_z = segments['velocity_z'].values

    # Estimate position by taking cumulative sums (simple integration of velocities)
    positions_x = np.cumsum(velocity_x * np.diff(times, prepend=times[0]))
    positions_y = np.cumsum(velocity_y * np.diff(times, prepend=times[0]))
    positions_z = np.cumsum(velocity_z * np.diff(times, prepend=times[0]))

    # Normalize time for color mapping
    norm = plt.Normalize(times.min(), times.max())

    # Create 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the 3D trajectory, coloring by time
    sc = ax.scatter(positions_x, positions_y, positions_z, c=times, cmap='plasma', norm=norm)

    # Add colorbar to indicate time progression
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label('Time (s)')

    # Label the axes
    ax.set_xlabel('X Position (m)')
    ax.set_ylabel('Y Position (m)')
    ax.set_zlabel('Z Position (m)')
    ax.set_title('3D Trajectory of Object Through Space')

    # Show the plot
    plt.show()
