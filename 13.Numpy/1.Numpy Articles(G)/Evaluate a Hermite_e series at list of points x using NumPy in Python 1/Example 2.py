# importing packages
import numpy as np
from numpy.polynomial import hermite as H

# array of coefficients
array = np.array([20,30,40,45])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# evaluating a hermite series at list of points x
print(H.hermval([2,3,4],array, tensor=False))
