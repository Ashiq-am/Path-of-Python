# Trimmed Mean

from scipy import stats
import numpy as np

arr1 = [[1, 3, 27],
		[5, 3, 18],
		[17, 16, 333],
		[3, 6, 82]]


# using axis = 0
print("\nTrimmed Mean is with default axis = 0 : \n",
	stats.tmean(arr1, axis = 1))
