# Python Program illustrating
# numpy.ravel() method

import numpy as geek

array = geek.arange(15).reshape(3, 5)
print("Original array : \n", array)

# Outpue comes like [ 0 1 2 ..., 12 13 14]
# as it is a long output, so it is the way of
# showing outptut in Python

# About :
print("\nAbout numpy.ravel() : ", array.ravel)

print("\nnumpy.ravel() : ", array.ravel())

# Maintaining both 'A' and 'F' order
print("\nMaintains A Order : ", array.ravel(order = 'A'))

# K-order preserving the ordering
# 'K' means that is neither 'A' nor 'F'
array2 = geek.arange(12).reshape(2,3,2).swapaxes(1,2)
print("\narray2 \n", array2)
print("\nMaintains A Order : ", array2.ravel(order = 'K'))
