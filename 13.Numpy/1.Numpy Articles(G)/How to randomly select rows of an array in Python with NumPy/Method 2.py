# import modules
import random
import numpy as np

# create 2D array
data = np.arange(50).reshape((5, 10))

# display original array
print("Array:")
print(data)

# row manipulation
rows_id = random.sample(range(0,
							data.shape[1]-1), 1)

# display random rows
print("\nRandom row:")
row = data[rows_id, :]
print(row)
