import numpy as np
from numpy.polynomial import hermite_e

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Dimensions of Array
print("Dimensions of Array: ", a.ndim)

# Shape of the array
print("\nShape of Array: ", a.shape)

# Tuple
x = (11, 12, 13, 14, 15)

# To evaluate a Hermite_e series at points x
print("\nHermite series at point", hermite_e.hermeval(x, a))
