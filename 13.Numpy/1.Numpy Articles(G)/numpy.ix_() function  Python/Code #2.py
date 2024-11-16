# Python program explaining
# numpy.ix_() function

# importing numpy as geek
import numpy as geek

arr = geek.arange(10).reshape(2, 5)
print("Initial array : \n", arr)

ixgrid = geek.ix_([0, 1], [2, 4])

print("New array : \n", arr[ixgrid])
