import pandas as pd
import matplotlib.pyplot as plt
import csv

def plot_acceleration(csv_file):
    """
    Plots acceleration (m/s²) vs time (s) from a CSV file.

    Args:
        csv_file (str): The path to the CSV file containing the data.
                         The CSV should have columns 'time' and 'acceleration'.
    """
    # Initialize lists for time and acceleration
    time = []
    acceleration = []

    # Read the CSV file using with open
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader)

        # Extract data
        for row in csv_reader:
            time.append(float(row[0]))
            acceleration.append(float(row[2]))

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(time, acceleration, marker='o', linestyle='-', color='b')
    plt.title('Acceleration vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s²)')
    plt.grid()
    plt.axhline(0, color='black', lw=0.8, ls='--')  # Add a horizontal line at y=0
    plt.show()

# Usage
csv_file = input("Enter the path to the CSV file: ")
try:
    plot_acceleration(csv_file)
except Exception as e:
    print(e)
