import csv
import math
import matplotlib.pyplot as plt

# Earth's radius in kilometers
EARTH_RADIUS_KM = 6371.0

def haversine_distance(lat1, lon1, alt1, lat2, lon2, alt2):
    """
    Calculate the distance between two GPS coordinates considering altitude.
    
    Parameters:
    lat1, lon1, alt1 -- Latitude, Longitude, and Altitude of point 1
    lat2, lon2, alt2 -- Latitude, Longitude, and Altitude of point 2
    
    Returns:
    Total distance in kilometers (considering both horizontal and vertical distances).
    """
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula to calculate horizontal distance
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Horizontal distance in kilometers
    horizontal_distance = EARTH_RADIUS_KM * c
    
    # Calculate the vertical distance from the difference in altitude (in kilometers)
    vertical_distance = (alt2 - alt1) / 1000.0  # Convert meters to kilometers
    
    # Total distance considering both horizontal and vertical components
    total_distance = math.sqrt(horizontal_distance**2 + vertical_distance**2)
    
    return total_distance

def read_gps_data(csv_file):
    """
    Read GPS data (with altitude) from a CSV file.
    
    Parameters:
    csv_file -- Path to the input CSV file
    
    Returns:
    A list of tuples containing (latitude, longitude, altitude).
    """
    gps_data = []
    
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                lat = float(row['Latitude (°)'])
                lon = float(row['Longitude (°)'])
                alt = float(row['Altitude (m)'])  # Read altitude from CSV in meters
                gps_data.append((lat, lon, alt))
    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
    except KeyError:
        print(f"Error: CSV file must contain 'Latitude (°)', 'Longitude (°)', and 'Altitude (m)' columns.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return gps_data

def calculate_distances(gps_data):
    """
    Calculate the distance between each pair of adjacent GPS points (considering altitude).
    
    Parameters:
    gps_data -- A list of tuples containing (latitude, longitude, altitude).
    
    Returns:
    A list of distances in kilometers between adjacent GPS points.
    """
    distances = []
    for i in range(len(gps_data) - 1):
        lat1, lon1, alt1 = gps_data[i]
        lat2, lon2, alt2 = gps_data[i + 1]
        distance = haversine_distance(lat1, lon1, alt1, lat2, lon2, alt2)
        distances.append(distance)
    
    return distances

def plot_gps_motion(gps_data, output_image):
    """
    Plot the GPS motion path (ignoring altitude) and save it as a PNG image.
    
    Parameters:
    gps_data -- A list of tuples containing (latitude, longitude, altitude).
    output_image -- Path to the output PNG file.
    """
    lats = [point[0] for point in gps_data]
    lons = [point[1] for point in gps_data]
    
    plt.figure(figsize=(8, 8))
    plt.plot(lons, lats, marker='o', color='b', linestyle='-', linewidth=2, markersize=5)
    
    plt.title("GPS Motion Path")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    
    # Save plot as PNG
    plt.savefig(output_image)
    plt.close()

def process_gps_data(csv_file, output_image):
    """
    Main function to read GPS data from a CSV, calculate distances between points (considering altitude), and plot the motion.
    
    Parameters:
    csv_file -- Path to the input CSV file.
    output_image -- Path to the output PNG image file.
    
    Returns:
    A list of distances between adjacent GPS points.
    """
    # Step 1: Read the GPS data
    gps_data = read_gps_data(csv_file)
    
    # Step 2: Calculate distances between adjacent points
    distances = calculate_distances(gps_data)
    
    # Step 3: Plot GPS motion and save as PNG (ignoring altitude)
    plot_gps_motion(gps_data, output_image)
    
    return distances

# Example usage
if __name__ == "__main__":
    csv_file = '/workspaces/CP1-24-midterm/Kylemasc917/data/Kylemasc011BWalkingTriangle.csv'
    output_image = 'gps_motion.png'
    
    distances = process_gps_data(csv_file, output_image)
    print("Distances between adjacent GPS points (in km):")
    print(distances)

if __name__ == "__main__":
    csv_file = '/workspaces/CP1-24-midterm/Kylemasc917/data/Kylemasc011DWalkingCircle.csv'
    output_image = 'gps_motion_circle.png'
    
    distances = process_gps_data(csv_file, output_image)
    print("Distances between adjacent GPS points (in km):")
    print(distances)
