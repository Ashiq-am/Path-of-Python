# Geometric Mean

from scipy.stats.mstats import gmean
arr1 = [[1, 3, 27],
		[3, 4, 6],
		[7, 6, 3],
		[3, 6, 8]]

print("Geometric Mean is :", gmean(arr1))

# using axis = 0
print("\nGeometric Mean is with default axis = 0 : \n",
	gmean(arr1, axis = 0))

# using axis = 1
print("\nGeometric Mean is with default axis = 1 : \n",
	gmean(arr1, axis = 1))
