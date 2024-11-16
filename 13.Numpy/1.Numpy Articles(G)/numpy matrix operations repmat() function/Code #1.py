# Python program explaining
# numpy.matlib.repmat() function

# importing numpy and matrix library
import numpy as geek
import numpy.matlib

# creating input array using
# array function
in_arr = geek.array([[1, 0, 2], [3, 4, 5]])
print("Input array", in_arr)

# making a new array
# using repmat() function
out_mat = geek.matlib.repmat(in_arr, 2, 3)
print ("Output repeated matrix : ", out_mat)
