# importing the required package
import numpy as np

# creating a numpy integer array
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print("First two columns")
print(arr1[0:2])

# printing columns in a range
print("Columns in a range")
print(arr1[4:7])

# computing length of array
length = len(arr1)

print("Last 3 Columns")
print(arr1[length-3:length])

print("Array till the end")
print(arr1[3:])
