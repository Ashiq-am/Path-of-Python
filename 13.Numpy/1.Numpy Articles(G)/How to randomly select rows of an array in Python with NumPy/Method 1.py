# import modules
import random
import numpy as np

# create 2D array
data = np.arange(50).reshape((5, 10))

# display original array
print("Array:")
print(data)

# row manipulation
np.random.shuffle(data)

# display random rows
print("\nRandom row:")
rows = data[:1, :]
print(rows)
