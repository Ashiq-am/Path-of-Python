import numpy as np
from scipy.stats import genlogistic

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = genlogistic.rvs(a, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = genlogistic.pdf(a, quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
