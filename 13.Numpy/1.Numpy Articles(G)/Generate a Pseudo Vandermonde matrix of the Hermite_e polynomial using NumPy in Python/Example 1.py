# import numpy and hermite_e libraries
import numpy as np
from numpy.polynomial import hermite_e

# Create an one dimensional array 'Arr'
Arr = np.array([2, 5, -3, 4])

# To generate a Vandermonde matrix of the
# Hermite_e polynomial,
# use the hermite_e.hermevander() method
print(hermite_e.hermevander(Arr, 2))
