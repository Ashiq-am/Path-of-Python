# import numpy and statsmodels
import numpy as np
from statsmodels.stats.stattools import jarque_bera

g = np.array([1, 2, 3])
# Using statsmodels.jarque_bera() method
gfg = jarque_bera(g)

print(gfg)
