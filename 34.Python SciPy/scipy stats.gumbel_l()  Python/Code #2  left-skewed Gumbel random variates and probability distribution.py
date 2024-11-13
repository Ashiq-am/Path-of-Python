import numpy as np
from scipy.stats import gumbel_l

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = gumbel_l.rvs(scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = gumbel_l.pdf(quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
