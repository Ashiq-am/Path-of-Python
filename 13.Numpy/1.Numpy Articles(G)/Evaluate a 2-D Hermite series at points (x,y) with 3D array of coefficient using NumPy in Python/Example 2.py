# importing numpy and hermite modules
import numpy as np
from numpy.polynomial import hermite

# Creating a 3D array of coefficients 'C'
C = np.arange(36).reshape(2,2,9)

# Evaluating the 2 dimentional hermite
# series ant x,y using
# hermval2d() funtion
x = [2,1]
y = [1,2]
print(hermite.hermval2d(x,y,C))
