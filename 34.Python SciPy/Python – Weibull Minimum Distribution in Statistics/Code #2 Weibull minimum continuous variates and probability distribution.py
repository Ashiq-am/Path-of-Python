import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = weibull_min .rvs(a, b, size = 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(weibull_min.ppf(0.01, a, b),
				weibull_min.ppf(0.99, a, b), 10)
R = weibull_min.pdf(x, 1, 3)
print ("\nProbability Distribution : \n", R)
