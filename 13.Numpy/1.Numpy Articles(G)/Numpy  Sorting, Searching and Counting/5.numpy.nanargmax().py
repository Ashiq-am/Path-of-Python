# Python Program illustrating
# working of nanargmax()

import numpy as geek

# Working on 1D array
array = [geek.nan, 4, 2, 3, 1]
print("INPUT ARRAY 1 : \n", array)

array2 = geek.array([[geek.nan, 4], [1, 3]])

# returning Indices of the max element
# as per the indices ingnoring NaN
print(("\nIndices of max in array1 : "
       , geek.nanargmax(array)))

# Working on 2D array
print("\nINPUT ARRAY 2 : \n", array2)
print(("\nIndices of max in array2 : "
       , geek.nanargmax(array2)))

print(("\nIndices at axis 1 of array2 : "
       , geek.nanargmax(array2, axis=1)))
