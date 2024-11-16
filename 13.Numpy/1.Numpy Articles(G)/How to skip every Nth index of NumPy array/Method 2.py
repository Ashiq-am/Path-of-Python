# importing required packages
import numpy as np

# declaring a numpy array
x = np.array([0, 1, 2, 3, 2, 5, 2, 7, 2, 9])

print("Original Array")
print(x)

# skipping third element
new_arr = x[np.mod(np.arange(x.size), 3) != 0]

print("Array after skipping elements : ")
print(new_arr)
