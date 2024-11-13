import numpy as np
from scipy.stats import chi2

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = chi2.rvs(a, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = chi2.pdf(a, quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
