import numpy as np


# Original array
array = np.arange(5)
print(array)

weights = np.arange(10, 15)
print(weights)

# Weighted average of the given array
res1 = np.average(array, weights=weights)
print(res1)
