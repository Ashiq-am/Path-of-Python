import numpy as np
from numpy.polynomial import hermite

a = np.array([0,1,0,0,2,3,4,5,0,0])

# Dimensions of Array
print("\nDimensions of Array:\n",a.ndim)

# Shape of the array
print("\nShape of Array:\n",a.shape)

# To remove small trailing
# coefficients from Hermite polynomial
print("\nResult:\n",hermite.hermtrim(a))
