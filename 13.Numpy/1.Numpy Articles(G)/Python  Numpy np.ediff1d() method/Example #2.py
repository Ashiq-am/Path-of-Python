# import numpy
import numpy as np

# using np.ediff1d() method
arr = np.array([1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
gfg = np.ediff1d(arr)

print(gfg)
