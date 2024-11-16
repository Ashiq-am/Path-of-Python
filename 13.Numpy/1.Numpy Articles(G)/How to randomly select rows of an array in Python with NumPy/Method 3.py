# import modules
import random
import numpy as np

# create 2D array
data = np.arange(50).reshape((5, 10))

# display original array
print("Array:")
print(data)

# row manipulation
number_of_rows = data.shape[0]
random_indices = np.random.choice(number_of_rows,
								size=1,
								replace=False)

# display random rows
print("\nRandom row:")
row = data[random_indices, :]
print(row)
