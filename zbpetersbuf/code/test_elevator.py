"""
tests code_tobenamedlatter.py

this was how i had to do it but no longer?
from zbpetersbuf.code.imp_to_metr import imptomec
print(vel[0].shape[0])
print(len(vel[1]))
print(vel[0][:,0])
print(1)
print(vel[1])
"""
from imp_to_metr import imptomec
from elevator import dimotion, pldimot, tampereddata

def test_imptomec():
    """This tests the ohmscur function"""
    assert imptomec(2, 'yard')==1.83
    assert imptomec(3, 'foot')==0.915


import pandas as pd
etot = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL05_eletot.csv')

vel = dimotion(etot)


pldimot(vel)


