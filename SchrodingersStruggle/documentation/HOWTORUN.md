# How to run

On each python file which contains modules specific to the task they are named after, there is a set of example code at the bottom which generally shows a way to utilize some functions in the document, such as plotting in gps_location.py

## Modules

The following specified modules have the intended purpose of establishing functions which allow the completion of one specific task. The other modules not specified with names beginning with 'test_' are for unit testing.

### gps_location.py Module

This creates functions which allow a variety of computations such as converting gps coordinates to spherical coordinates, converting spherical coordinates to cartesian, finding the distance between two gps positions, etc.

- total_distance:
 The derivation behind the equation used for the total_distance function is as follows:
\[

\]
### elevator_direction.py Module

The utilities module provides functionality like unit conversion functions, csv and metadata importing routines, and several different types of plotting methods.

For more information, see the module's docstrings as well as the example provided below for some basic use cases.

## Data Preparation

It is strongly recommended to use the following app for data collection, as this code was written specifically with its formatting in mind:
