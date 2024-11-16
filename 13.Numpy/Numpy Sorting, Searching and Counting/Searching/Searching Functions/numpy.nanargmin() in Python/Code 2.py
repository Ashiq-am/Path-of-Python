# Python Program illustarting
# working of nanargmin()

import numpy as geek

# Working on 2D array
array = ( [[ 8, 13, 5, 0],
		[ geek.nan, geek.nan, 5, 3],
		[10, 7, 15, 15],
		[3, 11, 4, 12]])
print("INPUT ARRAY : \n", array)

# returning Indices of the min element
# as per the indices

''' 
[[ 8 13 5 0] 
[ 0 2 5 3] 
[10 7 15 15] 
[ 3 11 4 12]] 
	^ ^ ^ ^ 
	0 2 4 0 - element 
	1 1 3 0 - indices 
'''

print("\nIndices of min using argmin : ", geek.argmin(array, axis = 0))
print("\nIndices of min using nanargmin : : ", geek.nanargmin(array, axis = 0))
