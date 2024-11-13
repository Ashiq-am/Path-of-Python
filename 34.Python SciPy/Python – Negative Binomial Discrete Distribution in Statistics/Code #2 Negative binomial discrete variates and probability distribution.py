import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = nbinom .rvs(a, b, size = 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(nbinom.ppf(0.01, a, b),
				nbinom.ppf(0.99, a, b), 10)
R = nbinom.ppf(x, 1, 3)
print ("\nProbability Distribution : \n", R)
