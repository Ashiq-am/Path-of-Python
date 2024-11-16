# importing the module
import numpy as np

# creating an array
arr = np.array([1, 3, 5, 7])
print("Original array: ")
print(arr)

# converting array elements into e ^ x
res = np.exp(arr)
print("\nPrinting e ^ x, element-wise of the said:")
print(res)
