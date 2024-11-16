import numpy as np
from numpy.polynomial import hermite

a = np.array([1,1,1,1,2,3,4,5,1,1])

# Dimensions of Array
print("\nDimensions of Array:\n",a.ndim)

# Shape of the array
print("\nShape of Array:\n",a.shape)

# To remove small trailing coefficients from Hermite polynomial
print("\nResult:\n",hermite.hermtrim(a,1))
