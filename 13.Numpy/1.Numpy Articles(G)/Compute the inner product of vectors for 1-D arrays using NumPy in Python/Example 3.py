# Importing library
import numpy as np

# Creating two 1-D arrays
array1 = np.array([1,2,2,8])
array2 = np.array([2,1,0,6])

print("Original 1-D arrays:")
print(array1)
print(array2)

# Output
print("Inner Product of the two array is:")
result = np.inner(array1, array2)
print(result)
