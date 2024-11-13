# Trimmed Maximum

from scipy import stats
import numpy as np

# array elements ranging from 0 to 19
x = [[1, 3, 27],
		[3, 4, 7],
		[7, 6, 3],
		[3, 6, 8]]

print("Trimmed Maximum :", stats.tmax(x))

# setting axis
print("\nTrimmed Maximum by setting axis : ",
	stats.tmax(x, axis = 1))

print("\nTrimmed Maximum by setting axis : ",
	stats.tmax(x, axis = 0))

# setting limit
print("\nTrimmed Maximum by setting limit : ",
	stats.tmax(x, (5), axis = 1))


print("\nTrimmed Maximum by setting limit : ",
	stats.tmax(x, (5), axis = 0))
