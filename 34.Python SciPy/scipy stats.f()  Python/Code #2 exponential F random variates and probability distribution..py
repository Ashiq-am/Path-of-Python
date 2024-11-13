import numpy as np
from scipy.io.matlab.tests.test_mio import a
from scipy.sparse.linalg.isolve.tests.demo_lgmres import f, b

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = f.rvs(a, b, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = f.pdf(a, b, quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
