# Trimmed Variance

from scipy import stats
import numpy as np

# array elements ranging from 0 to 19
x = np.arange(20)

print("Trimmed Variance :", stats.tvar(x))


print("\nTrimmed Variance by setting limit : ",
	stats.tvar(x, (2, 10)))
