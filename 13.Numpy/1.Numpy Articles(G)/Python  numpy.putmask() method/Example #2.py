# import numpy
import numpy as np

# using numpy.putmask() method
arr = np.array([[1, 2, 3],
				[3, 2, 1],
				[1, 2, 3]])

np.putmask(arr, arr>2, 4)

print(arr)
