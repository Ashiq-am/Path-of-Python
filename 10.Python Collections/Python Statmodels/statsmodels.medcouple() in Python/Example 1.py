# import numpy and statsmodels
import numpy as np
from statsmodels.stats.stattools import medcouple

g = np.array([1, 2, 3, 4, 7, 8])
# Using statsmodels.medcouple() method
gfg = medcouple(g)

print(gfg)
