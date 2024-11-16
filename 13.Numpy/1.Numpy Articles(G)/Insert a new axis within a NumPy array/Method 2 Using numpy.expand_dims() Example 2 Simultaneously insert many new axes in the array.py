import numpy as np


arr = np.arange(5*5).reshape(5,5)
print(arr.shape)

newaxes = (0, 3, -1)
arr_5D = np.expand_dims(arr, axis=newaxes)
print(arr_5D.shape)
