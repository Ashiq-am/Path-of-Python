# importing packages
import numpy as np
from numpy.polynomial import hermite as H

# array of coefficients
array = np.array([10,20,30,40])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# evaluating a hermite series at list of points x
print(H.hermval([1,2,3],array))
