import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = logser .rvs(a, b, size = 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(logser.ppf(0.01, a, b),
				logser.ppf(0.99, a, b), 10)
R = logser.ppf(x, 1, 3)
print ("\nProbability Distribution : \n", R)
