# stats.sem() method
import numpy as np
from scipy import stats


arr1 = [[20, 2, 7, 1, 34],
		[50, 12, 12, 34, 4]]

arr2 = [50, 12, 12, 34, 4]

print ("\narr1 : ", arr1)
print ("\narr2 : ", arr2)

print ("\nsem ratio for arr1 : ",
	stats.sem(arr1, axis = 0, ddof = 0))

print ("\nsem ratio for arr1 : ",
	stats.sem(arr1, axis = 1, ddof = 0))

print ("\nsem ratio for arr1 : ",
	stats.sem(arr2, axis = 0, ddof = 0))
