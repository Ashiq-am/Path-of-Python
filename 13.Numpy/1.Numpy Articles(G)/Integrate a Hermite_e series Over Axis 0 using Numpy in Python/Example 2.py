# import numpy and hermite_e libraries
import numpy as np
from numpy.polynomial import hermite_e

# create a multidimensional array
# 'arr' of coefficients
arr = np.arange(6).reshape(2,3)

# integrate a Hermite_e series using
# hermite_e.hermeint() function
print(hermite_e.hermeint(arr, axis = 0))
