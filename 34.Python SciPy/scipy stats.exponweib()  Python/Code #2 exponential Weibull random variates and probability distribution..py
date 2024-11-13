import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = exponweib .rvs(a, b, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = exponweib .pdf(a, b, quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
