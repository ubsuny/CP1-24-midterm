"""

this is not my code do not turn in

"""


import math as m
import numpy as np
import pandas as pd

def walkeq(walkdt):
    laloalt = list(zip(walkdt['Latitude (°)'], walkdt['Longitude (°)'], walkdt['Altitude WGS84 (m)']))
    a = 6378000  # Semi-major axis of the WGS84 ellipsoid
    f = 1 / 298.3  # Flattening
    b = (1 - f) * a  # Semi-minor axis
    s = np.zeros(walkdt.shape[0])  # Distance array
    l = abs(laloalt[0][1] - laloalt[1][1])  # Initial difference in longitude
    
    for i in range(walkdt.shape[0] - 1):
        phi1 = np.radians(laloalt[i][0])
        phi2 = np.radians(laloalt[i + 1][0])
        lam = np.radians(laloalt[i + 1][1] - laloalt[i][1])
        
        u1 = m.atan((1 - f) * m.tan(phi1))
        u2 = m.atan((1 - f) * m.tan(phi2))
        
        # Iterative calculation
        while True:
            sin_u1 = m.sin(u1)
            cos_u1 = m.cos(u1)
            sin_u2 = m.sin(u2)
            cos_u2 = m.cos(u2)
            sin_lam = m.sin(lam)
            cos_lam = m.cos(lam)
            
            sin_sigma = m.sqrt((cos_u2 * sin_lam) ** 2 + (cos_u1 * sin_u2 - sin_u1 * cos_u2 * cos_lam) ** 2)
            cos_sigma = sin_u1 * sin_u2 + cos_u1 * cos_u2 * cos_lam
            sigma = m.atan2(sin_sigma, cos_sigma)
            sin_alpha = cos_u1 * cos_u2 * sin_lam / m.sin(sigma)
            cos_sq_alpha = 1 - sin_alpha ** 2
            cos2sigma_m = cos_sq_alpha * (4 + f * (4 - 3 * cos_sq_alpha)) / 16
            
            c = f * cos_sq_alpha * (4 + f * (4 - 3 * cos_sq_alpha)) / 16
            lam_prev = lam
            lam = (l + (1 - c) * f * sin_sigma * (sigma + c * sin_sigma * (cos2sigma_m + c * cos_sigma * (2 * cos2sigma_m ** 2 - 1))))
            
            if abs(lam - lam_prev) < 1e-12:  # Convergence criteria
                break
        
        # Calculate the distance
        biga = 1 + (cos_sq_alpha * (u1 ** 2) / 16384) * (4096 + (cos_sq_alpha ** 2) * (320 - 175 * cos_sq_alpha ** 2))
        bigb = (cos_sq_alpha ** 2 / 1024) * (256 + (cos_sq_alpha ** 2) * (74 - 47 * cos_sq_alpha ** 2))
        
        dsf = bigb * m.sin(sigma)
        dsig = dsf * (m.cos(2 * sigma) + 0.25 * bigb * (m.cos(sigma) * (2 * m.cos(2 * sigma) ** 2 - 1) - (1 / 6) * bigb * m.cos(2 * sigma) * (4 * m.sin(sigma) ** 2 - 3) * (4 * m.cos(2 * sigma) ** 2 - 3)))
        
        s[i + 1] = b * biga * (sigma - dsig)
    
    return s

walk = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/walktest.csv')
print(walkeq(walk))
