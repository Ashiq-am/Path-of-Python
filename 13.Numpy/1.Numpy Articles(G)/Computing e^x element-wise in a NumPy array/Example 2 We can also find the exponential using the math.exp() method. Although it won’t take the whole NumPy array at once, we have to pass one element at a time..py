# importing the module
import numpy as np
import math

# creating an array
arr = np.array([1, 3, 5, 7])
print("Original array: ")
print(arr)

# converting array elements into e ^ x
res = []
for element in arr:
	res.append(math.exp(element))
print("\nPrinting e ^ x, element-wise of the said:")
print(res)
