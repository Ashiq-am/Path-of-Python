# Python Program illustarting
# working of argmin()

import numpy as geek

# Working on 2D array
array = geek.arange(10).reshape(2, 5)
print("array : \n", array)

array[0][0] = 10
array[1][1] = 1
array[0][1] = 1
print("\narray : \n", array)

# Returns min element
print("\narray : ", geek.argmin(array))

# First occurrence of an min element is given
print("\nmin ELEMENT INDICES : ", geek.argmin(array, axis=0))
