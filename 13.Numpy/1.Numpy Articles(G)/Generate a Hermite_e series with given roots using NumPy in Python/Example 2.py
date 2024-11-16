# import hermite_e library
from numpy.polynomial import hermite_e

# generate a Hermite_e series with given
# roots using hermefromroots() function
print(hermite_e.hermefromroots((-2, 4, 5, 4+5j)))
