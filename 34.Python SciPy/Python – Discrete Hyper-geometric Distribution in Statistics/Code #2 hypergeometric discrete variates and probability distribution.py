import numpy as np
from scipy.stats import hypergeom

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = hypergeom .pmf(a, b, c, 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(hypergeom.ppf(0.01, a, b, c),
				hypergeom.ppf(0.99, a, b, c), 10)
R = hypergeom.ppf(x, 1, 3, 3)
print ("\nProbability Distribution : \n", R)
