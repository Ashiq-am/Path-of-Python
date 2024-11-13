import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = truncnorm .rvs(a, b, size = 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(truncnorm.ppf(0.01, a, b),
				truncnorm.ppf(0.99, a, b), 10)
R = truncnorm.pdf(x, 1, 3)
print ("\nProbability Distribution : \n", R)
