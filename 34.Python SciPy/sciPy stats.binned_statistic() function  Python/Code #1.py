# stats.binned_statistic() method
import numpy as np
from scipy import stats

# 1D array
arr = [20, 2, 7, 1, 34]
print("\narr : \n", arr)


# median
print("\nbinned_statistic for median : \n", stats.binned_statistic(
		arr, np.arange(5), statistic ='median', bins = 4))
