"""doc string"""
import re
import os
import numpy as np

def gt_unix(mod_name):
    """docstring"""
    fpath='/workspaces/CP1-24-midterm/zbpetersbuf/data/'.strip()
    filpath = os.path.join(fpath, mod_name)

    with open(filpath, 'r', encoding='utf-8') as f:
        ftime = np.delete(re.findall(r'\d+', f.read()),0)

    matime = np.zeros(ftime.shape[0])
    for i in range(ftime.shape[0]):
        matime[i] = int(ftime[i])

    awf = [0,31,60,91,121,152,182,213,244,274,305,335]

    day = 365*(matime[0] - 1970) + matime[2] + awf[int(matime[1])] - max(0,((matime[0]-1972)//4))
    minit = 60*(max(matime[3]-matime[7],0)) + matime[4]
    sec = 86400*day + 60*minit + matime[5] + matime[6]*(10**(-3))

    return sec

asd=gt_unix('LL08_circle.md')
print(asd)
