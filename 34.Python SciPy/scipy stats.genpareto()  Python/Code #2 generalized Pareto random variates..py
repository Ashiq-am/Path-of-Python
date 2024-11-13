import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.stats import genpareto

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = genpareto.rvs(a, scale = 2, size = 10)
print ("Random Variates : \n", R)
