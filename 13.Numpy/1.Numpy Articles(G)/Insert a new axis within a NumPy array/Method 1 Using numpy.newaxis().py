import numpy as np


arr = np.arange(5*5).reshape(5, 5)
print(arr.shape)

# promoting 2D array to a 5D array
# arr[None, ..., None, None]
arr_5D = arr[np.newaxis, ..., np.newaxis, np.newaxis]

print(arr_5D.shape)
