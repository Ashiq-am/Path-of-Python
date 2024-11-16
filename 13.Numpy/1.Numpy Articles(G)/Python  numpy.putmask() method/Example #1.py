# import numpy
import numpy as np

# using numpy.putmask() method
arr = np.array([1, 2, 3, 4, 5, 6])
np.putmask(arr, arr % 2 == 0, 0)

print(arr)
