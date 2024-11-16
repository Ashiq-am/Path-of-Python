import numpy as np


# Original array
array = np.arange(5)
print(array)

weights = np.arange(10, 15)
print(weights)

# Weighted average of the given array
res2 = (array*(weights/weights.sum())).sum()
print(res2)
