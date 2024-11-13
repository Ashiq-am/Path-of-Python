# Trimmed Variance

from scipy import stats
import numpy as np

# array elements ranging from 0 to 19
x = np.arange(20)

# Setting limits
print("\nTrimmed Variance by setting limit : ",
	stats.tvar(x, (2, 10)))

# using flag
print("\nTrimmed Variance by setting limit : ",
	stats.tvar(x, (2, 10), (False, True)))

print("\nTrimmed Variance by setting limit : ",
	stats.tvar(x, (2, 12), (True, False)))
