# importing numpy and Hermite_e libraries
import numpy as np
from numpy.polynomial import hermite_e as H

# Creating an array 'Arr'
Arr1 = [2, 3, 5, 6, 9]

# To convert a polynomial to a Hermite series,
# use the hermite_e.poly2herme() function
# present in Python Numpy module
print(H.poly2herme(Arr1))
