# stats.binned_statistic_2d() method
import numpy as np
from scipy import stats

x = np.random.rand(10)
y = np.random.rand(10)
z = np.arange(10)

# mean
print ("\nbinned_statistic_2d for mean : ",
	stats.binned_statistic_2d(x, y, values = z,
				statistic ='mean', bins = [5, 5]))
