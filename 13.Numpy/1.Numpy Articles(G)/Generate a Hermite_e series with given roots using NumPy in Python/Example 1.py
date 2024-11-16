# import hermite_e library
from numpy.polynomial import hermite_e

# create an array 'arr' of roots
arr = [1, 0, -2]

# generate a Hermite_e series with given
# roots using hermefromroots() function
print(hermite_e.hermefromroots(arr))
