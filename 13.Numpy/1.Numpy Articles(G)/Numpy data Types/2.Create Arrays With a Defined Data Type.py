# Import NumPy Array
import numpy as np

# Creating a float64 array
arr1 = np.array([1, 2, 3, 4], dtype=np.float64)

# Creating a 3x3 int32 array of zeros
arr2 = np.zeros((3, 3), dtype=np.int32)

# Creating a 2x2 complex128 array of ones
arr3 = np.ones((2, 2), dtype=np.complex128)

# Creating a 1D bool array
arr4 = np.empty((4,), dtype=np.bool_)

# Print the arrays and their data types
print("arr1:\n", arr1)
print("Data type of arr1:", arr1.dtype)

print("\narr2:\n", arr2)
print("Data type of arr2:", arr2.dtype)

print("\narr3:\n", arr3)
print("Data type of arr3:", arr3.dtype)

print("\narr4:\n", arr4)
print("Data type of arr4:", arr4.dtype)
