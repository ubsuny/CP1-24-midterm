"""doc string"""
import matplotlib as m
import numpy as np
import pandas as pd
import re

def gt_unix(mod_name):
    with open('/workspaces/CP1-24-midterm/zbpetersbuf/data/'mod_name, 'r') as f:
        return np.delete(re.findall(r'\d+', f.read()),0)



asd=gt_unix('LL08_circle.md')


print(asd)