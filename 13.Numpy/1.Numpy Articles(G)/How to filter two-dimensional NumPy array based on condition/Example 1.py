import numpy as np


arr = np.asarray([[1, 'one'], [2, 'two'], [3, 'three'],
				[4, 'four'], [5, 'five']])

fltr = np.asarray(['two', 'four'])
arr[np.in1d(arr[:, 1], fltr)]
