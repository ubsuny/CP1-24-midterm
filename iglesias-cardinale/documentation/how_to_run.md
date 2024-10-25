# How to run the code in the iglesias-cardinale folder

To use the functions in any of the modules, create a Jupyter Notebook file and import the desired modules.

If you are interested in calculating the distances between two points, plotting position versus time, or making a 2d or 3d map of positions from GPS data, use the distance.py module and import it like this:

```python
from distance import *
```

To calculate the distance between two points, use either the ```python gps_distance_flat_earth``` function or the ```python gps_distance_wgs84``` function.
To plot position versus time or make a map of positions, make use of the ``` python gps_wgs84 ``` function.

