import numpy as np

arr = np.array([])
arr = np.hstack((arr, np.array(['G', 'F', 'G'])))
print(arr)

arr = np.vstack((arr, np.array(['G', 'F', 'G'])))
print(arr)
