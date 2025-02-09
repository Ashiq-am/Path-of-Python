import numpy as np

# Create a 1D array
array1 = np.array([1, 3, 5, 7, 9, 11])

# Reshape the 1D array into a 2D array (2 rows and 3 columns)
array2 = np.reshape(array1, (2, 3))
print(\"Original array:\
\", array1)
print("\
Reshaped array:\", array2)