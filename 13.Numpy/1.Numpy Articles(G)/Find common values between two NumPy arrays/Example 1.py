import numpy as np


ar1 = np.array([0, 1, 2, 3, 4])
ar2 = [1, 3, 4]

# Common values between two arrays
print(np.intersect1d(ar1, ar2))
