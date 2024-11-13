import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.optimize.tests.test_lsq_linear import b
from scipy.stats import burr

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = burr.rvs(a, b, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = burr.pdf(quantile, a, b, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
