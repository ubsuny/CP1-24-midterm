"""i got all of this from chat gbt so dont run"""
import os
import matplotlib.pyplot as plt

# Sample plot (ensure you've created a plot)
plt.plot([1, 2, 3], [4, 5, 6])

save_plot = input("Do you want to save the plot? (yes/no): ").strip().lower()

if save_plot == 'yes':
    folder_path = input("Enter the folder path where you want to save the plot: ").strip()
    
    # Ensure the path exists
    if not os.path.exists(folder_path):
        print("The specified directory does not exist. Please check the path.")
    else:
        filename = "simple_line_plot.png"
        file_path = os.path.join(folder_path, filename)
        
        plt.savefig(file_path, format='png')
        print(f"Plot saved as {file_path}")
else:
    print("Plot not saved.")

