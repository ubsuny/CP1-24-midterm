"""
imp_to_metr.py

"""
def imptomec(x,lenguni):
    """enter your mesuremtn value and then the kind of mesurment, ie if feet enter ft, feet or foot
    if its yards enter yards, yard or yd"""
    if lenguni == 'yard':
        x = 3*x
    return 0.305*x

print(imptomec(1,'yard'))
print(imptomec(1,'yards'))
