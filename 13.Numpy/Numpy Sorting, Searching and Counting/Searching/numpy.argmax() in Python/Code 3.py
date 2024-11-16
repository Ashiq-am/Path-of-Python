# Python Program illustarting
# working of argmax()

import numpy as geek

# Working on 2D array
array = geek.arange(10).reshape(2, 5)
print("array : \n", array)

array[0][1] = 6
print("\narray : \n", array)

# Returns max element
print("\narray : ", geek.argmax(array))

# First occurrence of an max element is given
print("\nMAX ELEMENT INDICES : ", geek.argmax(array, axis=0))
