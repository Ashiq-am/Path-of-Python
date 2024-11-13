# scoreatpercentile
from scipy import stats
import numpy as np

arr = [[14, 17, 12, 33, 44],
	[15, 6, 27, 8, 19],
	[23, 2, 54, 1, 4, ]]

print("arr : ", arr)

print ("\nScore at 50th percentile : ",
	stats.scoreatpercentile(arr, 50))

print ("\nScore at 50th percentile : ",
	stats.scoreatpercentile(arr, 50, axis = 1))

print ("\nScore at 50th percentile : ",
	stats.scoreatpercentile(arr, 50, axis = 0))
