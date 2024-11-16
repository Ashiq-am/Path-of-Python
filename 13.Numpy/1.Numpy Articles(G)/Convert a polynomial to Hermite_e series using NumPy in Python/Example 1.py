# importing numpy and Hermite_e libraries
import numpy as np
from numpy.polynomial import hermite_e

# Creating an array 'Arr' using the
# numpy.array()
Arr = np.array([4, 7, 9, 10, 15])

# To convert a polynomial to a Hermite series,
# use the hermite_e.poly2herme() function
# present in Python Numpy module
print(hermite_e.poly2herme(Arr))
