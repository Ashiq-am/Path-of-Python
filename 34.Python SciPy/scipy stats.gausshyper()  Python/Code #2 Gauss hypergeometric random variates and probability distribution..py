import numpy as np
from scipy.stats import gausshyper

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = gausshyper .rvs(a, b, c, z, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = gausshyper .pdf(a, b, c, z, quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
