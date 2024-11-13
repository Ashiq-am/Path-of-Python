import numpy as np
from scipy.stats import betaprime

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = betaprime.rvs(a, b, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = betaprime.pdf(quantile, a, b, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
