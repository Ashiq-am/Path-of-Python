import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.sparse.linalg.isolve.tests.demo_lgmres import b
from scipy.stats import dlaplace

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = dlaplace .rvs(a, b, size = 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(dlaplace.ppf(0.01, a, b),
				dlaplace.ppf(0.99, a, b), 10)
R = dlaplace.ppf(x, 1, 3)
print ("\nProbability Distribution : \n", R)
