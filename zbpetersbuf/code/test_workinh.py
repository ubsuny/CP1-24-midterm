"""
test_workinh.py
this moduale is the unit test for workinh.py
"""

import pandas as pd
from workinh import walkeq, distbetp, gpsloc, plwalk

walk = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL07_circle.csv')
exmp = walkeq(walk)
print(sum(exmp))

print(distbetp(exmp,2))
