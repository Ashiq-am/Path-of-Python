# Python Program explaining
# working of numpy.bincount() method

import numpy as geek

# 1D array with +ve integers
array2 = [10, 11, 4, 6, 2, 1, 9]
array1 = [1, 3, 1, 3, 1, 2, 2]

# array2 : weight
bin = geek.bincount(array1, array2)
print("Summation element-wise : \n", bin)

#index 0 : 0
#index 1 : 10 + 4 + 2 = 16
#index 2 : 1 + 9 = 10
#index 3 : 11 + 6 = 17
