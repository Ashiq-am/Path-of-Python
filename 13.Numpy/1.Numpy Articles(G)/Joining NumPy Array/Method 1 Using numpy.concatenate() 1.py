import numpy as np

array_1 = np.array([[1, 2], [3, 4]])
array_2 = np.array([[5, 6], [7, 8]])

array_new = np.concatenate((array_1, array_2), axis=1)
print(array_new)
