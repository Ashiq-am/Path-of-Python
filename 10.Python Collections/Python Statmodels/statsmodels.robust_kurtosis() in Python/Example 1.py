# import numpy and statsmodels
import numpy as np
from statsmodels.stats.stattools import robust_kurtosis

g = np.array([1, 2, 3, 4, 7, 8])
# Using statsmodels.robust_kurtosis() method
gfg = robust_kurtosis(g)

print(gfg)
