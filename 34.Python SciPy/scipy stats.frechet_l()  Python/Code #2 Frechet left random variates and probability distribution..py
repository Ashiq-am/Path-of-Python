import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.stats import frechet_l

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = frechet_l.rvs(a, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = frechet_l.pdf(a, quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
