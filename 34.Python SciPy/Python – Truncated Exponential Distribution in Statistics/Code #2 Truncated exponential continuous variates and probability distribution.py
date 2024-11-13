import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = truncexpon .rvs(a, b, size = 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(truncexpon.ppf(0.01, a, b),
				truncexpon.ppf(0.99, a, b), 10)
R = truncexpon.pdf(x, 1, 3)
print ("\nProbability Distribution : \n", R)
