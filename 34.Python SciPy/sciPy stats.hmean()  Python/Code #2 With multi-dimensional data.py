# Harmonic Mean

from scipy.stats.mstats import hmean
arr1 = [[1, 3, 27],
		[3, 4, 6],
		[7, 6, 3],
		[3, 6, 8]]

print("\nHarmonic Mean is :", hmean(arr1))

# using axis = 0
print("\nHarmonic Mean is with default axis = 0 : \n",
	hmean(arr1, axis = 0))

# using axis = 1
print("\nHarmonic Mean is with default axis = 1 : \n",
	hmean(arr1, axis = 1))
