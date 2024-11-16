import numpy as np

# Create an array with float data type elements
arr_original = np.array([1.2, 2.5, 3.7])

# Converting to int32
arr_new = arr_original.astype(np.int32)

# Print the original its type
print("Original array:", arr_original)
print("Data type of original array:", arr_original.dtype)

# Print new array and its type
print("\nNew array:", arr_new)
print("Data type of new array:", arr_new.dtype)
