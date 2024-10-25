"""
This module is to plot the tracing of the motion
"""

from plotting_functions_module import two_dimensional_plot, multi_plot
from mercator_projection_functions import xy_on_earth
from distance_calculator_module import longitudes_gt_4, latitudes_gt_4, longitudes_gc_4, latitudes_gc_4
from direction_of_motion_module import times_ad_4, velocity_unit_vectors_ad_4, times_au_4, velocity_unit_vectors_au_4

# Obtaining the planar locations
# for the triangle
x_gt_4, y_gt_4 = xy_on_earth(latitudes_gt_4, longitudes_gt_4)
# for the circle
x_gc_4, y_gc_4 = xy_on_earth(latitudes_gc_4, longitudes_gc_4)
# Now plotting
# for the triangle
two_dimensional_plot(x_gt_4, y_gt_4, "gt004_gps_triangle", "x (km)", "y (km)",
                     "/workspaces/CP1-24-midterm/HeshamElsaman/Data/GPSTriangle/gt004_gps_triangle/Location GPS 2024-10-20 19-36-53/gt004_gps_triangle.png")
# for the circle
two_dimensional_plot(x_gc_4, y_gc_4, "gc004_gps_circle", "x (km)", "y (km)",
                     "/workspaces/CP1-24-midterm/HeshamElsaman/Data/GPSCircle/gc004_gps_circle/Location GPS 2024-10-20 18-16-03/gc004_gps_circle.png")

# Parsing the directions data for the downward motion
times_list_ad_4 = [times_ad_4, times_ad_4, times_ad_4]
directions_list_ad_4 = list([[i[0] for i in velocity_unit_vectors_ad_4],
                             [j[1] for j in velocity_unit_vectors_ad_4],
                             [k[2] for k in velocity_unit_vectors_ad_4]])
title_ad_4 = "directions over time"
horizontal_label_ad_4 = "t (s)"
vertical_label_ad_4 = "n"
filename_ad_4 = "/workspaces/CP1-24-midterm/HeshamElsaman/Data/AccelerationDown/ad004_acceleration_down/Acceleration without g 2024-10-20 20-18-58/ad004_acceleration_down.png"
legends_ad_4 = ["x-direction", "y-direction", "z-direction"]
line_plot_ad_4 = False
# Plotting the directions
multi_plot(times_list_ad_4, directions_list_ad_4, title_ad_4, horizontal_label_ad_4,
           vertical_label_ad_4, filename_ad_4, legends_ad_4, line_plot_ad_4)

# Parsing the directions data for the upward motion
times_list_au_4 = [times_au_4, times_au_4, times_au_4]
directions_list_au_4 = list([[i[0] for i in velocity_unit_vectors_au_4],
                             [j[1] for j in velocity_unit_vectors_au_4],
                             [k[2] for k in velocity_unit_vectors_au_4]])
title_au_4 = "directions over time"
horizontal_label_au_4 = "t (s)"
vertical_label_au_4 = "n"
filename_au_4 = "/workspaces/CP1-24-midterm/HeshamElsaman/Data/AccelerationUp/au004_acceleration_up/Acceleration without g 2024-10-20 20-17-14/au004_acceleration_up.png"
legends_au_4 = ["x-direction", "y-direction", "z-direction"]
line_plot_au_4 = False
# Plotting the directions
multi_plot(times_list_au_4, directions_list_au_4, title_au_4, horizontal_label_au_4,
           vertical_label_au_4, filename_au_4, legends_au_4, line_plot_au_4)
