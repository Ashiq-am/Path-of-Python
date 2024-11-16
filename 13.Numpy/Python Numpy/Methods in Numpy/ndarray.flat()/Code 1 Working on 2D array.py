# Python Program illustrating
# working of ndarray.flat()

import numpy as geek

# Working on 1D iteration of 2D array
array = geek.arange(15).reshape(3, 5)
print("2D array : \n",array )

# Using flat() : 1D iterator over range
print("\nUsing Array : ", array.flat[2:6])

# Using flat() to Print 1D repersented array
print("\n1D representation of array : \n ->", array.flat[0:15])
