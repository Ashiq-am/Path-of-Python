# Python Program illustrating
# working of ndarray.flat()

import numpy as geek

# Working on 1D iteration of 2D array
array = geek.arange(15).reshape(3, 5)
print("2D array : \n",array )

print("\nID array : \n", array.flat[0:15])

print("\nType of array,flat() : ", type(array.flat))

for i in array.flat:
	print(i, end = ' ')
