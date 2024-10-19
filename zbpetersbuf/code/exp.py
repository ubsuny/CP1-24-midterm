"""i got all of this from chat gbt so dont run"""

import matplotlib.pyplot as plt
import os

# Your data
x = [1, 2, 3]
y = [1, 2, 3]

# Create a new figure
plt.figure()

# Plot the data
plt.plot(x, y, marker='o')  # Add markers for better visibility

# Add labels and title
plt.title('Simple Line Plot')
plt.xlabel('X values')
plt.ylabel('Y values')

# Show the grid
plt.grid()

# Display the plot
plt.show()

# Ask the user if they want to save the plot
save_plot = input("Do you want to save the plot? (yes/no): ").strip().lower()

if save_plot == 'yes':
    # Get the current working directory
    current_directory = os.getcwd()
    
    # Specify the filename
    filename = "exmp.png"
    
    # Create the full path for saving
    file_path = os.path.join(current_directory, filename)
    
    # Save the plot
    plt.savefig(file_path, format='png')
    print(f"Plot saved as {file_path}")
else:
    print("Plot not saved.")

