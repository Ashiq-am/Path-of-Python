# import numpy and statsmodels
import numpy as np
from statsmodels.stats.stattools import expected_robust_kurtosis

# Using statsmodels.expected_robust_kurtosis() method
gfg = expected_robust_kurtosis()

print(gfg)
