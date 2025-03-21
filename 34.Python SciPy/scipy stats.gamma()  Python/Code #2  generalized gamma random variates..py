import numpy as np
from scipy.stats import gamma

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = gamma.rvs(a, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = gamma.pdf(a, quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
