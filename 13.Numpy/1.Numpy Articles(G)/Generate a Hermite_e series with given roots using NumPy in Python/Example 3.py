# import hermite_e library
from numpy.polynomial import hermite_e
import numpy

# create an array 'arr' of roots
arr = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])

# generate a Hermite_e series with given
# roots using hermefromroots() function
print(hermite_e.hermefromroots(arr))
