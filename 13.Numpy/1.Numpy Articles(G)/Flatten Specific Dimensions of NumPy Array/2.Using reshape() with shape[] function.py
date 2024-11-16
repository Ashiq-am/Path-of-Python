import numpy as np
arr = np.zeros((5, 2, 5))
flattened_arr = arr.reshape(-2, arr.shape[-2])
print(flattened_arr)
