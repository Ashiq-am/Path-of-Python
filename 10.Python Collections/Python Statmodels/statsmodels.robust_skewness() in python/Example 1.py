# import numpy and statsmodels
import numpy as np
from statsmodels.stats.stattools import robust_skewness

g = np.array([1, 2, 3, 4, 7, 8])
# Using statsmodels.robust_skewness() method
gfg = medcouple(g)

print(gfg)
