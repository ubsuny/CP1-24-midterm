# The midterm project is divided in the following parts:

1. Data: The data files are as follows:
    i. OA11_elevator_upward_run.csv (contains acceleration(without g) data for elevator going from lowest to tomost floor)
    ii. OA11_elevator_downward_run.csv (contains acceleration(without g) data for elevator going from lowest to tomost floor)
    iii. OA11_gps_circle_run.csv (contains GPS data for the circular track)
    iv. OA11_gps_triangle_run.csv (contains GPS data for the triangular track)

    The corresponding markdown files contain the metadata that includes Author Name, Date, Time (GMT), Location and Weather Conditions for each experiment.

2. Code: The code files are as follows:
    i. unit_converter.py :  python module to convert distance in yard/foot to metre.
    ii gps_distance.py : python module to obtain the distance between two adjacent GPS positions (Haversine distance, assuming the Earth as a sphere)[1,2].
    iii. elevator_direction_of_motion.py : python module to generate the velocity based on acceleration data from the elevator, hence obtaining the direction of motion.
    iv. unix_time_converter.py : python module to read date and time data from the markdown meta files and convert that into Unix time.[3]
    v. test_*.py : files are the corresponding unit tests for the above modules using the pytest framework.

    To run any of the module, call them using the standard terminal commands and import the function to be used. Provide the file paths as "ojha-aditya/data/<experimentname.csv>".

3. Documentation: The documentation files include:
    i. how_to_run.md : this markdown file
    ii. references.md : the bibliography file
    iii. elevator_direction_of_motions.png : the graphs depict the change in velocity as we move up and down in the elevator, and also the corresponding directions of motion. The discrepancy in plots is due to improper calibration of measuring device i.e. cellphone.
    iv. gps_motions.png : xy plot of GPS data showing the trajectory as triangle and circle
    
