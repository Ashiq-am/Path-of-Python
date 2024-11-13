# import numpy and statsmodels
import numpy as np
from statsmodels.stats.stattools import omni_normtest

g = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Using statsmodels.omni_normtest() method
gfg = omni_normtest(g)

print(gfg)
