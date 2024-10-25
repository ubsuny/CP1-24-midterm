"""This module reads acceleration data from a CSV file, calculates motion direction, 
and plots the motion path in x, y, and z directions over time."""

import numpy as np
import matplotlib.pyplot as plt

def read_acceleration_data(csv_file):
    """Read acceleration data from a CSV file.
    
    Args:
        csv_file (str): Path to the CSV file.
        
    Returns:
        np.ndarray: Array with columns [time, x_acc, y_acc, z_acc].
    """
    try:
        data = np.genfromtxt(csv_file, delimiter=',', skip_header=1)
        if data.shape[1] != 4:
            raise ValueError("CSV file should have exactly four columns: time, x, y, z")
        return data
    except IOError:
        print(f"Error: Could not read file {csv_file}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None

def calculate_position(data):
    """Calculate position using numerical integration of acceleration data.
    
    Args:
        data (np.ndarray): Array containing time, x_acc, y_acc, z_acc.
        
    Returns:
        tuple: Three arrays (x_position, y_position, z_position) representing position over time.
    """
    time = data[:, 0]
    x_acc = data[:, 1]
    y_acc = data[:, 2]
    z_acc = data[:, 3]

    # Calculate time intervals, prepend first interval as 0
    dt = np.diff(time, prepend=time[0])

    # Velocity integration from acceleration (v = ∫a dt)
    x_velocity = np.cumsum(x_acc * dt)
    y_velocity = np.cumsum(y_acc * dt)
    z_velocity = np.cumsum(z_acc * dt)

    # Position integration from velocity (s = ∫v dt)
    x_position = np.cumsum(x_velocity * dt)
    y_position = np.cumsum(y_velocity * dt)
    z_position = np.cumsum(z_velocity * dt)

    return x_position, y_position, z_position

def plot_motion(x_position, y_position, z_position, gen_pic):
    """Plot motion in x, y, and z directions over time and save as an image.
    
    Args:
        x_position (np.ndarray): X position over time.
        y_position (np.ndarray): Y position over time.
        z_position (np.ndarray): Z position over time.
        gen_pic (str): Path where to save the generated image.
    """
    plt.figure(figsize=(15, 10))

    # Plot X Position
    plt.subplot(3, 1, 1)
    plt.plot(x_position, color='r', linewidth=2)
    plt.title("X Position over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("X Position (m)")
    plt.grid()

    # Plot Y Position
    plt.subplot(3, 1, 2)
    plt.plot(y_position, color='g', linewidth=2)
    plt.title("Y Position over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Y Position (m)")
    plt.grid()

    # Plot Z Position
    plt.subplot(3, 1, 3)
    plt.plot(z_position, color='b', linewidth=2)
    plt.title("Z Position over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Z Position (m)")
    plt.grid()

    plt.tight_layout()
    plt.savefig(gen_pic)
    plt.close()
    print(f"Motion plot saved as {gen_pic}")

def process_acceleration_data(csv_file, gen_pic):
    """Main function to process acceleration data and plot motion.

    Args:
        csv_file (str): Path to the CSV file with acceleration data.
        gen_pic (str): File path for saving the plot.
    """
    data = read_acceleration_data(csv_file)
    if data is None:
        return None

    x_position, y_position, z_position = calculate_position(data)
    plot_motion(x_position, y_position, z_position, gen_pic)
    return x_position, y_position, z_position

# Usage Example
if __name__ == "__main__":
    csv_file_input = input("Enter the path to the CSV file: ")
    output_image = "motion_plot.png"
    try:
        process_acceleration_data(csv_file_input, output_image)
    except Exception as e:
        print(f"Error during processing: {e}")
