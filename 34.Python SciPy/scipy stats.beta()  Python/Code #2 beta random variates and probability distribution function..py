import numpy as np
from scipy.stats import beta

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = beta.rvs(a, b, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = beta.pdf(quantile, a, b, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
