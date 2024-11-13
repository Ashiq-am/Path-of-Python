# import numpy and statsmodels
import numpy as np
from statsmodels.stats.stattools import robust_kurtosis

g = np.array([1, 2, 8, 9, 10])
# Using statsmodels.robust_kurtosis() method
gfg = robust_kurtosis(g)

print(gfg)
