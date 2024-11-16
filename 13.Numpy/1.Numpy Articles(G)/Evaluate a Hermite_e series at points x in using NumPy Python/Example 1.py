import numpy as np
from numpy.polynomial import hermite as H

# array of coefficients
array = np.array([5,6,7,8])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# evaluating a hermite series at points x
print(H.hermval(1,array))
