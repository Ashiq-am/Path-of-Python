# import numpy and statsmodels
import numpy as np
from statsmodels.stats.stattools import durbin_watson

g = np.array([1, 2, 3])
# Using statsmodels.durbin_watson() method
gfg = durbin_watson(g)

print(gfg)
