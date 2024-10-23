import pandas as pd
from datetime import datetime

def convert_to_unix_time_from_csv(file_path):
    """
    Reads date and time from a CSV file and converts it to Unix time.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    list: A list of Unix timestamps corresponding to the date and time in the file.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Combine the Date and Time columns into a single datetime string
    df['datetime'] = df['Date'] + ' ' + df['Time']
    
    # Convert the datetime string to a datetime object and then to Unix time
    df['unix_time'] = df['datetime'].apply(lambda x: int(datetime.strptime(x, "%Y-%m-%d %H:%M:%S").timestamp()))
    
    return df[['datetime', 'unix_time']]  # Return the datetime and Unix time columns

# List of all CSV files
file_paths = [
    'data/gps_data_1.csv',  # Replace with actual file paths
    'data/gps_data_2.csv',
    'data/gps_data_3.csv',
    'data/gps_data_4.csv'
]

# Loop through each file, convert the date and time to Unix time, and print the result
for file_path in file_paths:
    unix_time_data = convert_to_unix_time_from_csv(file_path)
    print(f"Unix Time Data for {file_path}:")
    print(unix_time_data)
    print('-' * 50)  # Separator for better readability
