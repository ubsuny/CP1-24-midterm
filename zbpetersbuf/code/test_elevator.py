"""
tests code_tobenamedlatter.py

"""
from imp_to_metr import imptomec
from elevator import dimotion, pldimot

def test_imptomec():
    """This tests the ohmscur function"""
    assert imptomec(2, 'yard')==1.83
    assert imptomec(3, 'foot')==0.915


import pandas as pd
etot = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL05_eletot.csv')

vel = dimotion(etot)

pldimot(vel)
