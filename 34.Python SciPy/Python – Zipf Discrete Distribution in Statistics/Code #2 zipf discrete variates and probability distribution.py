import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = zipf .pmf(a, b)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(zipf.ppf(0.01, a, b),
				zipf.ppf(0.99, a, b), 10)
R = zipf.ppf(x, 1, 3)
print ("\nProbability Distribution : \n", R)
