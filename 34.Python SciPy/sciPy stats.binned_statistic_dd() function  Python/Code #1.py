# stats.binned_statistic_dd() method
import numpy as np
from scipy import stats

x = np.ones(10)
y = np.ones(10)

print ("x : \n", x)
print ("\ny : \n", y)

print ("\nbinned_statistic_2d for count : ",
	stats.binned_statistic_dd([x, y], None, 'count', bins = 3))
