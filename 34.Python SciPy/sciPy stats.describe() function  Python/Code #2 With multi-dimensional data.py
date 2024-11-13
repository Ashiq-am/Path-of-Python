# FInding statistics of data

from scipy import stats

arr1 = [[1, 3, 27],
		[3, 4, 6],
		[7, 6, 3],
		[3, 6, 8]]

desc = stats.describe(arr1, axis = 0)


print("No. of observations at axis = 0 :\n\n", desc)


print("\n\nNo. of observations at axis = 1 :\n\n", desc)
