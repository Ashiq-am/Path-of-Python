import numpy as np
from scipy.stats import gengamma

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = gengamma.rvs(a, b, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = gengamma.pdf(a, b, quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
