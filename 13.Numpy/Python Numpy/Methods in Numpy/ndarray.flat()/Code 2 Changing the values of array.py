# Python Program illustrating
# working of ndarray.flat()

import numpy as geek

# Working on 1D iteration of 2D array
array = geek.arange(15).reshape(3, 5)
print("2D array : \n",array )

# All elements set to 1
array.flat = 1
print("\nAll Values set to 1 : \n", array)

array.flat[3:6] = 8
array.flat[8:10] = 9
print("Changing values in a range : \n", array)
