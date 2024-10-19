"""
tests code_tobenamedlatter.py

this was how i had to do it but no longer?
from zbpetersbuf.code.imp_to_metr import imptomec
"""
from imp_to_metr import imptomec

def test_imptomec():
    """This tests the ohmscur function"""
    assert imptomec(2, 'yard')==1.83
    assert imptomec(3, 'foot')==0.915

print(imptomec(2,'yard')==1.83)
print(imptomec(2,'Yd')==1.83)