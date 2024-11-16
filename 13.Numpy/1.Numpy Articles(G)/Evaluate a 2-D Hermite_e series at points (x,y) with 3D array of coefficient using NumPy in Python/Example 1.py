# import packages
import numpy as np
from numpy.polynomial import hermite_e as mit

# array of coefficients
array = np.array([[[5,6],[7,8],[9,10]]])
print(array)

# shape of the array is
print("Shape of the array is : ",array.shape)

# dimension of the array
print("The dimension of the array is : ",array.ndim)

# evaluating a 2-d hermite series at point(x,y)
# with 3D coeffiecients
print(mit.hermeval2d([1,1],[2,2],array))
