import numpy as np
from scipy import stats

arr2 = [[50, 12, 12, 34, 4],
		[12, 11, 10, 34, 21]]

print ("\nZ-score for arr2 : \n", stats.zscore(arr2, axis = 0))
print ("\nZ-score for arr2 : \n", stats.zscore(arr2, axis = 1))
