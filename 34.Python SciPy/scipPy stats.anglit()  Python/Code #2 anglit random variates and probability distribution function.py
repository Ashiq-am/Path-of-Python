import numpy as np
from scipy.stats import anglit

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = anglit.rvs(scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = anglit.pdf(quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
