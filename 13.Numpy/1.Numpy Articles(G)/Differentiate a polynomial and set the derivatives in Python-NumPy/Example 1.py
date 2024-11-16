import numpy as np
from numpy.polynomial import polynomial as P

# Creating an array of polynomial coefficients
c = np.array([5,6,7,8])
print(c)
# shape of the array is
print("Shape of the array is : ",c.shape)

# dimension of the array
print("The dimension of the array is : ",c.ndim)

# Datatype of the array
print("Datatype of our Array is : ",c.dtype)


# To differentiate a polynomial.
print(P.polyder(c, 3))
