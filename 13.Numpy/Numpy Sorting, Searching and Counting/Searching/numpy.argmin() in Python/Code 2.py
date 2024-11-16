# Python Program illustarting
# working of argmin()

import numpy as geek

# Working on 2D array
array = geek.random.randint(16, size=(4, 4))
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
print("\nIndices of min element : ", geek.argmin(array, axis = 0))
