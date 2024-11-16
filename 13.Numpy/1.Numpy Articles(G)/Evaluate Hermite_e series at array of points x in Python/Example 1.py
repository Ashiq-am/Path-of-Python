# importing necessary libraries
import numpy as np
from numpy.polynomial import hermite_e as H

# Create an array of coefficients
c = np.array([3, 5, 7])

# To evaluate a Hermite_e series at points x,
# use the hermite.hermeval() method in Python Numpy
x = np.array([[2, 3], [5, 6]])
print("Result : \n", H.hermeval(x, c))
