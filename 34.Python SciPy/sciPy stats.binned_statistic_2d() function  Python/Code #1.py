# stats.binned_statistic_2d() method
import numpy as np
from scipy import stats

x = np.random.rand(10)
y = np.random.rand(10)

z = np.arange(10)

print ("x : \n", x)
print ("\ny : \n", y)
print ("\nz : \n", z)

# count
print ("\nbinned_statistic_2d for count : ",
	stats.binned_statistic_2d(x, y, values = z,
				statistic ='count', bins = [5, 5]))
