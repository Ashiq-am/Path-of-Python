# Import the numpy library
import numpy as np

# Create a NumPy ndarray
arr = np.array([50, 60, 70])

# Convert the ndarray to a tuple
tuple_arr = tuple(map(tuple, arr))

# Creating a set
fixed_set = set()

# Adding numpy array to set
fixed_set.add(tuple_arr)

# Print the ndarray
print(fixed_set)
