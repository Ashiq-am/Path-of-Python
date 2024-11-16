# import numpy and hermite_e libraries
import numpy as np
from numpy.polynomial import hermite_e as HE

# Create a multidimensional array 'Arr'
# of coefficients
Arr = np.matrix([[1, 3], [4, 5]])

# To evaluate a Hermite_e series at points
# x for multidimensional coefficient array 'Arr',
# use the hermite.hermeval() method in
# Python Numpy
print(HE.hermeval([2, 3], Arr))
