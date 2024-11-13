import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.optimize.tests.test_lsq_linear import b
from scipy.stats import bernoulli

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = bernoulli .rvs(a, b, size = 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(bernoulli.ppf(0.01, a, b),
				bernoulli.ppf(0.99, a, b), 10)
R = bernoulli.ppf(x, 1, 3)
print ("\nProbability Distribution : \n", R)
