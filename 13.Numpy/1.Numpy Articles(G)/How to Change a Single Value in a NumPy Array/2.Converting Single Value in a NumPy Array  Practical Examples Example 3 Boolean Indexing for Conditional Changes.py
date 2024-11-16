import numpy as np

# Create a 5x5 NumPy array with values from 1 to 25
array = np.arange(1, 26).reshape(5, 5)
# Change all values greater than 20 to 100
array[array > 20] = 100
print("\nArray after changing values greater than 20 using boolean indexing:\n", array)
