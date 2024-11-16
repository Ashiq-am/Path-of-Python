# Import NumPy library

import numpy as np

# Create an array using the list

np_arr1 = np.array([23, 11, 45, 43, 60, 18,
					33, 71, 52, 38])
print("The values of the input array :\n", np_arr1)


# Create another array based on the
# multiple conditions and one array
new_arr1 = np.where((np_arr1))

# Print the new array
print("The filtered values of the array :\n", new_arr1)

# Create an array using range values
np_arr2 = np.arange(40, 50)

# Create another array based on the
# multiple conditions and two arrays
new_arr2 = np.where((np_arr1), np_arr1, np_arr2)

# Print the new array
print("The filtered values of the array :\n", new_arr2)
