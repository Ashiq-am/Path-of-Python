# importing libraries
import numpy as np
from scipy import stats

# using np.ones for x and y
x = np.ones(10)
y = np.ones(10)

# Using binned_statistic_dd
print ("\nbinned_statistic_2d for count : ",
		stats.binned_statistic_dd([x, y], None,
		'count', bins=3, range=[[2,3],[0,0.5]]))
