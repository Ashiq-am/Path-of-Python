import numpy as np

data = np.array([1, 2, 3, 4, 5])
empty_slice = data[5:2]
output = np.mean(empty_slice)
print(output)
