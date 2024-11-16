# import library
import numpy as np

# list
x = [12, 13, 14, 15, 16]
y = [17, 18, 19, 20, 21]

# create a numpy 2d-array
array = np.array([x, y]).reshape((2, 5))

print("original array:\n", array)

# find max and min elements
# row-wise
max1, min1 = np.amax(array, 1), np.amin(array,1)

# print the row-wise max
# and min difference
print("Difference:\n", max1 - min1)
