"""
This module contains utility functions that do not belong as first order
members of the Trip class.

List out classes and functions:...

"""
from datetime import datetime
import pandas as pd
import numpy as np
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
        'feet': 0.3048,        # Feet to meters (exact quantity)
        'yd': 0.9144,        # Yards to meters (exact quantity)
        'yard': 0.9144,        # Yards to meters (exact quantity)
        'mile': 1609.344,      # Miles to meters (exact quantity)
        'ml': 1609.344      # Miles to meters (exact quantity)
    }

    # sanitize plural units
    if unit.endswith('s'):  # if the unit is pluralized
        unit = unit[:-1]    # make it singular

    # make sure the unit is in our dict
    if unit not in conversion_factors:
        raise ValueError(f"Unknown unit: {unit}")
    # Convert the value using the conversion factor for the unit
    quantity = value * conversion_factors[unit]
    # and return it
    return quantity

def convert_to_feet(value, unit):
    """
    Converts a given value from a specified unit to feet. This function
    uses exact quantities for conversion factors where possible.

    Args:
        value (number): The numerical value to be converted.
        unit (str): The unit of the value to convert from. Supported units
        include:
                    'm' (meters), 'km' (kilometers), 'inch' (inches),
                    'yd' (yards), 'mile' (miles), 'cm' (centimeters), 'mm' (millimeters).

    Returns:
        Number: The equivalent value in feet (a float).

    Raises:
        ValueError: If the specified unit is not supported.
    """
    # sanitize units
    if unit.endswith('s'):  # if the unit is pluralized
        unit = unit[:-1]    # make it singular

    # Define conversion factors for various units to feet
    conversion_factors_to_feet = {
        'm': 1250/381,         # Exact: 1 m = 1250/381 feet
        'meter': 1250/381,     # Exact based on IYPA of 1959 (see references)
        'km': 1250000/381,     # Kilometers to feet (exact)
        'inch': 1/12,          # Inches to feet (exact, 1 foot = 12 inches)
        'in': 1/12,            # Inches to feet (exact)
        'cm': 1250/381000,     # Centimeters to feet (exact)
        'mm': 1250/3810000,    # Millimeters to feet (exact)
        'yd': 3.0,             # Yards to feet (exact)
        'yard': 3.0,           # Yards to feet (exact)
        'mile': 5280.0,        # Miles to feet (exact)
        'mi': 5280.0           # Miles to feet (exact)
    }

    # make sure the unit key exists
    if unit not in conversion_factors_to_feet:
        raise ValueError(f"Unknown unit: {unit}")
    # Convert the value using the conversion factor for the unit
    quantity = value * conversion_factors_to_feet[unit]
    # and return it
    return quantity

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

def haversine_with_altitude(start_point, end_point):
    """
    Calculate the 3D great-circle distance between two points on the spherical
    Earth surface, including the Euclidean altitude difference.

    The output distance is in meters.

    Args:
        start_point (dict): A dictionary with 'lat', 'lon', and 'alt' keys
            representing the start point's
        latitude, longitude, and altitude.
        end_point (dict): A dictionary with 'lat', 'lon', and 'alt' keys
            representing the end point's latitude, longitude, and altitude.

    Returns:
        distance (float): The 3D distance between the two points in meters.
    """
    radius_earth = 6371.0  # Radius of Earth in kilometers

    # Convert degrees to radians
    lat1 = np.radians(start_point['lat'])
    lon1 = np.radians(start_point['lon'])
    lat2 = np.radians(end_point['lat'])
    lon2 = np.radians(end_point['lon'])

    # Differences in latitudes, longitudes, and altitudes
    dlat = lat2 - lat1  # Latitude difference in radians
    dlon = lon2 - lon1  # Longitude difference in radians
    dalt = end_point['alt'] - start_point['alt']  # Altitude difference in meters

    # Haversine formula for the distance over the Earth's surface (in kilometers)
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    surface_distance_km = radius_earth * c  # Distance in kilometers

    # Convert surface distance from km to meters
    surface_distance_m = surface_distance_km * 1000  # Convert to meters

    # 3D Euclidean distance, including altitude
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

    # get the trip segments
    segments = gps_trip.segments

    # Check if necessary columns exist in the segments DataFrame
    if not {'start_long', 'start_lat', 'end_long', 'end_lat'}.issubset(segments.columns):
        print("Error: Missing longitude or latitude data in segments.")

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

    segments = gps_trip.segments

    # Check if necessary columns exist in the segments DataFrame
    if not {
        'start_long',
        'start_lat',
        'end_long',
        'end_lat',
        'start_t',
        'stop_t'
    }.issubset(segments.columns):
        # columns are missing, report
        print("Error: Missing longitude, latitude, or time data in segments.")

    # Normalize time data to range from 0 to 1 for color mapping
    times = segments['start_t'].values
    norm = plt.Normalize(times.min(), times.max())  # Normalize the time range

    # Create the color map (from red to purple)
    cmap = "plasma"

    plt.figure(figsize=(10, 6))

    # Plot each segment with color corresponding to its start time
    longitudes = np.concatenate([segments['start_long'].values, segments['end_long'].values])
    latitudes = np.concatenate([segments['start_lat'].values, segments['end_lat'].values])

    # use the start times for coloring
    colors = np.concatenate([segments['start_t'].values, segments['start_t'].values])

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

def plot_acceltrip_acceleration_with_color(accel_trip,
                                            component='total',
                                            compression_factor=1.0,
                                            connect_points=True,
                                            step=1):
    """
    Plots the specified acceleration component (x, y, z, or total) of an AccelTrip
    object over time, with color representing the direction and magnitude of
    acceleration. Red indicates higher positive acceleration, and purple indicates
    lower or negative acceleration.

    Args:
        accel_trip (AccelTrip): An AccelTrip object with segment data containing
            time and acceleration components.
        component (str):
            The acceleration component to plot ('x', 'y', 'z', or 'total').
            Defaults to 'total'.
        compression_factor (float):
            Factor to compress the center of the color spectrum. Defaults to 1.0.
        connect_points (bool):
            Whether to connect points with lines. Defaults to True.
        step (number):
            Plot every Nth point to reduce the number of points displayed.
            Defaults to 1 (plot all points).

    Returns:
        None: Displays the plot using Matplotlib.
    """
    if accel_trip.segments is None:
        print("Error: No segment data available to plot.")
        return

    segments = accel_trip.segments

    # Determine which acceleration component to plot
    if component == 'x':
        accel_column = 'accel_x'
    elif component == 'y':
        accel_column = 'accel_y'
    elif component == 'z':
        accel_column = 'accel_z'
    elif component == 'total':
        accel_column = 'total_acceleration'
    else:
        print(f"Error: Invalid component '{component}'. Must be 'x', 'y', 'z', or 'total'.")
        return

    # Check if the necessary columns exist in the segments DataFrame
    if not {'start_t', accel_column}.issubset(segments.columns):
        print(f"Error: Missing time or {component}-acceleration data in segments.")
        return

    # Extract time and the chosen acceleration component, using step to downsample data
    times = segments['start_t'].values[::step]
    acceleration = segments[accel_column].values[::step]

    # Apply compression to the acceleration values to broaden the color spectrum
    compressed_acceleration = (np.sign(acceleration) *
        (np.abs(acceleration) ** (1 / compression_factor)))

    # Normalize the compressed acceleration values for color mapping
    norm = plt.Normalize(compressed_acceleration.min(), compressed_acceleration.max())

    # Create the color map (from purple to red)
    cmap = "nipy_spectral"

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Optionally connect points with lines
    if connect_points:
        plt.plot(
            times,
            acceleration,
            color='gray',
            alpha=0.7,
            label=f'{component.capitalize()} Acceleration'
        )

    # Plot points with color representing the acceleration magnitude and direction
    sc = plt.scatter(
        times,
        acceleration,
        c=compressed_acceleration,
        cmap=cmap,
        norm=norm,
        marker='o'
    )

    # Create colorbar to indicate acceleration magnitude and direction
    cbar = plt.colorbar(sc)
    cbar.set_label(f'Scaled {component.capitalize()} Acceleration (m/s²)')

    # Label the axes
    plt.xlabel('Time (s)')
    plt.ylabel(f'{component.capitalize()} Acceleration (m/s²)')

    title = f"{component.capitalize()}"
    title += "Acceleration over Time for AccelTrip (Colored by Acceleration Direction)"
    plt.title(title)

    # Add grid and legend
    plt.grid(True)

    if connect_points is True:
        plt.legend()

    # Show the plot
    plt.show()
    return plt

def plot_acceltrip_velocity(accel_trip, component='z'):
    """
    Plots the specified velocity component (x, y, or z) of an AccelTrip object
    over time.

    Args:
        accel_trip (AccelTrip): An AccelTrip object with segment data containing
            time and velocity components.
        component (str): The velocity component to plot ('x', 'y', or 'z').
            Defaults to 'z'.

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

def plot_acceltrip_velocity_with_acceleration_color(
        accel_trip,
        component='z',
        compression_factor=1.0,
        step=10):
    """
    Plots the specified velocity component (x, y, or z) of an AccelTrip object
    over time, with color representing the direction of acceleration. Red
    indicates positive acceleration, and purple indicates negative acceleration.

    A compression factor is applied to the acceleration values to control the
    color spectrum, making a wider range of colors visible (compressing the
    center dominance).

    Args:
        accel_trip (AccelTrip): An AccelTrip object with segment data containing
        time and velocity components.

        component (str): The velocity component to plot ('x', 'y', or 'z').
            Defaults to 'z'.
        compression_factor (float): Factor to compress the center of the color
            spectrum. Defaults to 1.0.
        step (int): Downsampling factor, plotting every Nth point. Defaults to 10.

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
    times = segments['start_t'].values[::step]  # Downsample by selecting every Nth point
    velocity = segments[velocity_column].values[::step]

    # Calculate the change in velocity (acceleration) between consecutive points
    acceleration = np.diff(velocity, prepend=velocity[0])

    # Apply compression to the acceleration values to broaden the color spectrum
    compressed_acceleration = (
        np.sign(acceleration) * (np.abs(acceleration) ** (1 / compression_factor))
    )

    # Normalize the compressed acceleration values for color mapping
    norm = plt.Normalize(compressed_acceleration.min(), compressed_acceleration.max())

    # Create the color map (from purple to red)
    cmap = "nipy_spectral"

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Plot lines between points
    plt.plot(
        times,
        velocity,
        color='gray',
        alpha=0.7,
        label=f'{component.upper()}-Velocity'
    )

    # Use scatter to plot points with colors based on the compressed acceleration direction
    sc = plt.scatter(
        times,
        velocity,
        c=compressed_acceleration,
        cmap=cmap,
        norm=norm,
        marker='o'
    )

    # Create colorbar to indicate acceleration direction
    cbar = plt.colorbar(sc)
    cbar.set_label('Scaled Acceleration (m/s²)')

    # Label the axes
    plt.xlabel('Time (s)')
    plt.ylabel(f'{component.upper()}-Velocity (m/s)')

    # set the title of the plot
    title = f'{component.upper()}'
    title += '-Velocity over Time for AccelTrip (Colored by Acceleration Direction)'
    plt.title(title)

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

def plot_3d_trajectory(accel_trip):
    """
    Plots the 3D trajectory of an AccelTrip object using cumulative sums of the
    velocity components to approximate position. The color of the trajectory
    represents the time progression. The axes are normalized so that the axis
    with the largest range determines the scale for all axes.

    Args:
        accel_trip (AccelTrip): An AccelTrip object with segment data containing
        velocity components.

    Returns:
        None: Displays the 3D plot using Matplotlib.
    """
    if accel_trip.segments is None:
        print("Error: No segment data available to plot.")
        return

    segments = accel_trip.segments

    if not {'start_t', 'velocity_x', 'velocity_y', 'velocity_z'}.issubset(segments.columns):
        print("Error: Missing velocity or time data in segments.")
        return

    # Extract necessary data into dictionaries for better organization
    data = {
        'times': segments['start_t'].values,
        'velocities': {
            'x': segments['velocity_x'].values,
            'y': segments['velocity_y'].values,
            'z': segments['velocity_z'].values
        }
    }

    # Estimate positions by integrating velocity over time
    positions = {
        axis: np.cumsum(data['velocities'][axis] * np.diff(data['times'], prepend=data['times'][0]))
        for axis in ['x', 'y', 'z']
    }

    # Find ranges of each axis
    ranges = {
        axis: positions[axis].max() - positions[axis].min()
        for axis in ['x', 'y', 'z']
    }

    max_range = max(ranges.values())  # Find the largest range

    # Normalize positions based on the largest axis range
    positions_normalized = {
        axis: (positions[axis] - positions[axis].min()) / ranges[axis] * max_range
        for axis in ['x', 'y', 'z']
    }

    # Normalize time for color mapping
    norm = plt.Normalize(data['times'].min(), data['times'].max())

    # Create 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the 3D trajectory, coloring by time
    sc = ax.scatter(positions_normalized['x'], positions_normalized['y'], positions_normalized['z'],
                    c=data['times'], cmap='plasma', norm=norm)

    # Add colorbar to indicate time progression
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label('Time (s)')

    # Label the axes with normalization indicated
    ax.set_xlabel('X Position (normalized)')
    ax.set_ylabel('Y Position (normalized)')
    ax.set_zlabel('Z Position (normalized)')
    ax.set_title('Normalized 3D Trajectory of Object Through Space')

    # Set equal scale for all axes
    ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

    # Show the plot
    plt.show()


def render_multiplot(list1, list2, save_path='multiplot.png'):
    """
    Renders two lists of plots into a single multiplot arranged in two columns.

    Args:
        list1 (list): The first list of plot functions or plot data to be rendered in the left column.
        list2 (list): The second list of plot functions or plot data to be rendered in the right column.
        save_path (str): The file path where the PNG will be saved.

    Returns:
        None: Saves the multiplot PNG to the specified path.
    """
    # Determine the number of rows based on the longest list
    num_rows = max(len(list1), len(list2))

    # Create a figure with two columns and num_rows rows
    fig, axes = plt.subplots(num_rows, 2, figsize=(10, 5 * num_rows))

    # If there's only one row, axes will not be a 2D array, so we need to ensure it's iterable.
    if num_rows == 1:
        axes = [axes]

    # Plot the first list in the left column
    for i, plot_func in enumerate(list1):
        if i < num_rows:
            axes[i, 0].set_title(f'Plot {i+1} (Left)')
            plot_func(axes[i, 0])  # Pass the axis to the plot function

    # Plot the second list in the right column
    for i, plot_func in enumerate(list2):
        if i < num_rows:
            axes[i, 1].set_title(f'Plot {i+1} (Right)')
            plot_func(axes[i, 1])  # Pass the axis to the plot function

    # Remove any empty subplots (in case the lists are not the same length)
    for i in range(len(list1), num_rows):
        fig.delaxes(axes[i, 0])
    for i in range(len(list2), num_rows):
        fig.delaxes(axes[i, 1])

    # Adjust layout
    plt.tight_layout()

    # Save the multiplot as a PNG
    plt.savefig(save_path)
    plt.close()
