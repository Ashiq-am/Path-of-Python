import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.sparse.linalg.isolve.tests.test_lsqr import b
from scipy.stats import geom

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = geom .rvs(a, b, size = 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(geom.ppf(0.01, a, b),
				geom.ppf(0.99, a, b), 10)
R = geom.ppf(x, 1, 3)
print ("\nProbability Distribution : \n", R)
