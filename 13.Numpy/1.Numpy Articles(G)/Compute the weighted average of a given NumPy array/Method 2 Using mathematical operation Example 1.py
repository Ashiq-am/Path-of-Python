import numpy as np


# Original array
array = np.arange(2, 7)
print(array)

weights = np.arange(2, 7)
print(weights)

# Weighted average of the given array
res2 = (array*(weights/weights.sum())).sum()
print(res2)
