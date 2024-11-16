# Python Program illustarting
# working of nanargmax()

import numpy as geek

# Working on 2D array
array = ([[8, 13, 5, 0],
          [16, geek.nan, 5, 3],
          [geek.nan, 7, 15, 15],
          [3, 11, 4, 12]])
print("INPUT ARRAY : \n", array)

# returning Indices of the max element
# as per the indices

''' 
[[ 8 13 5 0] 
[ 16 2 5 3] 
[10 7 15 15] 
[ 3 11 4 12]] 
	^ ^ ^ ^ 

'''

print("\nIndices of max using argmax : ", geek.argmax(array, axis=0))
print("\nIndices of max using nanargmax : : ", geek.nanargmax(array, axis=0))
