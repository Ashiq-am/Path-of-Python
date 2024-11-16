# Python Program illustarting
# working of argmax()

import numpy as geek

# Working on 2D array
array = geek.random.randint(16, size=(4, 4))
print("INPUT ARRAY : \n", array)

# No axis mentioned, so works on entire array
print("\nMax element : ", geek.argmax(array))

# returning Indices of the max element
# as per the indices

''' 
[[ 0 3 8 13] 
	[12 11 2 11] 
	[ 5 13 8 3] 
	[12 15 3 4]] 
	^ ^ ^ ^ 
	12 15 8 13 - element 
	1 3 0 0 - indices 
'''
print("\nIndices of Max element : ", geek.argmax(array, axis=0))

''' 
							ELEMENT INDEX 
->[[ 0 3 8 13]		 13	 3 
	->[12 11 2 11]		 12	 0 
	->[ 5 13 8 3]		 13	 1 
	->[12 15 3 4]]		 15	 1 

'''
print("\nIndices of Max element : ", geek.argmax(array, axis=1))
