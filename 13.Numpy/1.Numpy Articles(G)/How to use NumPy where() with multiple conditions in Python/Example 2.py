# Import NumPy library

import numpy as np

# Create two arrays of random values
np_arr1 = np.random.rand(10)*100
np_arr2 = np.random.rand(10)*100


# Print the array values
print("\nThe values of the first array :\n", np_arr1)
print("\nThe values of the second array :\n", np_arr2)


# Create a new array based on the conditions
new_arr = np.where((np_arr1), np_arr1, np_arr2)

# Print the new array
print("\nThe filtered values of both arrays :\n", new_arr)
