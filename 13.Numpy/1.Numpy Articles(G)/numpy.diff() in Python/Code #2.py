# Python program explaining
# numpy.diff() method


# importing numpy
import numpy as geek

# input array
arr = geek.array([[1, 2, 3, 5], [4, 6, 7, 9]])

print("Input array : ", arr)
print("Difference when axis is 0 : ", geek.diff(arr, axis=0))
print("Difference when axis is 1 : ", geek.diff(arr, axis=1))
