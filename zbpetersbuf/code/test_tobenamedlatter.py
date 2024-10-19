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
from direcofmov_fromaccdata import dimotion, pldimot

def test_imptomec():
    """This tests the ohmscur function"""
    assert imptomec(2, 'yard')==1.83
    assert imptomec(3, 'foot')==0.915

print(imptomec(2,'yard')==1.83)
print(imptomec(2,'Yd')==1.83)

import pandas as pd
eup = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL01_eupdata.csv')
edn = pd.read_csv('/workspaces/CP1-24-midterm/zbpetersbuf/data/LL02_edndata.csv')

vel = dimotion(eup)

import matplotlib.pyplot as plt


x=[1,2,3]
y=[1,2,3]
plt.figure()
plt.plot(x,y, marker='o')
plt.title('exampl')
plt.savefig('exampl', format='png')
print(plt.show())
