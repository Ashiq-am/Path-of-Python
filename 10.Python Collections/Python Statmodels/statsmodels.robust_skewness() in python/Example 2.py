# import numpy and statsmodels
import numpy as np
from statsmodels.stats.stattools import robust_skewness

g = np.array([1, 2, 8, 9, 10])
# Using statsmodels.robust_skewness() method
gfg = medcouple(g)

print(gfg)
