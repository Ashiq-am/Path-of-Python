import numpy as np

# Create three arrays with different data types
array1 = np.array([1, 2, 3], dtype=np.int32)
array2 = np.array([1.5, 2.5, 3.5], dtype=np.float64)
array3 = np.array(['a', 'b', 'c'], dtype=object)

# Combine arrays horizontally using np.hstack
combined_array = np.hstack((array1, array2, array3))
print("Array 1:")
print(array1)
print("Array 2:")
print(array2)
print("Array 3:")
print(array3)
print("Combined Array:")
print(combined_array)
