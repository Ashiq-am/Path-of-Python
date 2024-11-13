# stats.binned_statistic() method
import numpy as np
from scipy import stats

# mean
arr = [20, 2, 7, 1, 34]
print("\nbinned_statistic for mean : \n", stats.binned_statistic(
		arr, np.arange(5), statistic ='mean', bins = 2))
