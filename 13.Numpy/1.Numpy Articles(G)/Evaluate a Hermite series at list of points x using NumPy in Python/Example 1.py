import numpy as np
from numpy.polynomial import hermite

a = np.array([1,2,3,4,5])

# Dimensions of Array
print("Dimensions of Array: ",a.ndim)

# Shape of the array
print("\nShape of Array: ",a.shape)

# List
x = [6,7,8,9,10]

# To evaluate a Hermite series at points x
print("\nHermite series at point", hermite.hermval(x,a))
