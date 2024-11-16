# Python Program illustrating
# working of argmin()

import numpy as geek

# Working on 1D array
array = geek.arange(8)
print("INPUT ARRAY : \n", array)


# returning Indices of the min element
# as per the indices
print("\nIndices of min element : ", geek.argmin(array, axis=0))
