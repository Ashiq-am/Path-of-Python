import numpy as np

try:
    # Example operation that may cause an error
    arr = np.array([1, 2, 'three'])
    arr_sum = np.sum(arr)
except TypeError as e:
    print("TypeError occurred:", e)