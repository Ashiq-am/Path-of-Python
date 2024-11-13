# Trimmed Minimum

from scipy import stats
import numpy as np

# array elements ranging from 0 to 19
x = [1, 3, 27, 56, 2, 4, 13, 3, 6]

print("Trimmed Minimum :", stats.tmin(x))


print("\nTrimmed Minimum by setting limit : ",
	stats.tmin(x, (5)))
