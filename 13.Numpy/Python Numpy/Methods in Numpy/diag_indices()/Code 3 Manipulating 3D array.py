# Python Program illustrating
# working of diag_indices()

import numpy as geek

# Setting diagonal indices
d = geek.diag_indices(1, 2)
print("Diag indices : \n", d)

# Creating a 3D array with all ones
array = geek.ones((2, 2, 2), dtype=geek.int)
print("Initial array : \n", array)

# Manipulating a 3D array
array[d] = 0
print("New array : \n", array)
