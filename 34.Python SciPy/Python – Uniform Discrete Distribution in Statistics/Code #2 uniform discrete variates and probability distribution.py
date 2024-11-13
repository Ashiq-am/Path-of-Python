import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = randint .rvs(a, b, size = 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(randint.ppf(0.01, a, b),
				randint.ppf(0.99, a, b), 10)
R = randint.ppf(x, 1, 3)
print ("\nProbability Distribution : \n", R)
