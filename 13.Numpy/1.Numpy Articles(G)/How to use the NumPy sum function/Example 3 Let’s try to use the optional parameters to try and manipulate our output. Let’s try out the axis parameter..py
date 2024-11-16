# Import NumPy
import numpy as np

# Initialize our array
array = [[0, 1], [0, 5]]

# Let's say we want to sum each sub array
# Sums will be returned seperately in array
# format Call sum() function
print(np.sum(array, axis = 1))
