# Python Program explaining
# working of numpy.bincount() method

import numpy as geek

# 1D array with +ve integers
array1 = [1, 6, 1, 1, 1, 2, 2]
bin = geek.bincount(array1)
print("Bincount output : \n ", bin)
print("size of bin : ", len(bin), "\n")

array2 = [1, 5, 5, 5, 4, 5, 5, 2, 2, 2]
bin = geek.bincount(array2)
print("Bincount output : \n ", bin)
print("size of bin : ", len(bin), "\n")

# using min_length attribute
length = 10
bin1 = geek.bincount(array2, None, length)
print("Bincount output : \n ", bin1)

print("size of bin : ", len(bin1), "\n")
