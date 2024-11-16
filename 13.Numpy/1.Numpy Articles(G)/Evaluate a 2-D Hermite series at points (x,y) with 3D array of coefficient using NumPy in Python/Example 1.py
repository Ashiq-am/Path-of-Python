# importing numpy and hermite modules
import numpy as np
from numpy.polynomial import hermite

# Creating a 3D array of coefficients 'C'
C = np.array([ [[0,1,2], [3,4,5]], [[6,7,8], [9,10,11]] ])

# Evaluating the 2 dimentional hermite
# series ant x,y using
# hermval2d() funtion
print(hermite.hermval2d([1,2],[1,2],C))
