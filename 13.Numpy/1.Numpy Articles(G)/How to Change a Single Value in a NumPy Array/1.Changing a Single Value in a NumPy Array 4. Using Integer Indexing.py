import numpy as np

# Create a 5x5 NumPy array with values from 1 to 25
array = np.arange(1, 26).reshape(5, 5)
print("Original Array:\n", array)
# Change the value at row index 2 and column index 3
array[2, 3] = 99
print("\nArray after changing a single value using integer indexing:\n", array)
