# Trimmed Minimum

from scipy import stats
import numpy as np

# array elements ranging from 0 to 19
x = [[1, 3, 27],
	[3, 4, 7],
	[7, 6, 3],
	[3, 6, 8]]

print("Trimmed Minimum :", stats.tmin(x))

# setting axis
print("\nTrimmed Minimum by setting axis : ",
	stats.tmin(x, axis = 1))

print("\nTrimmed Minimum by setting axis : ",
	stats.tmin(x, axis = 0))

# setting limit
print("\nTrimmed Minimum by setting limit : ",
	stats.tmin(x, (5), axis = 1))


print("\nTrimmed Minimum by setting limit : ",
	stats.tmin(x, (5), axis = 0))
