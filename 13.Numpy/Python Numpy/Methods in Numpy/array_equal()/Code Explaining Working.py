# Python program explaining
# array_equal() function
import numpy as np

# input
arr1 = np.arange(4)
arr2 = [7, 4, 6, 7]
print ("arr1 : ", arr1)
print ("arr2 : ", arr2)

print ("\nResult : ", np.array_equal(arr1, arr2))

arr1 = np.arange(4)
arr2 = np.arange(4)
print ("\n\narr1 : ", arr1)
print ("arr2 : ", arr2)

print ("\nResult : ", np.array_equal(arr1, arr2))

arr1 = np.arange(4)
arr2 = np.arange(5)
print ("\n\narr1 : ", arr1)
print ("arr2 : ", arr2)

print ("\nResult : ", np.array_equal(arr1, arr2))
