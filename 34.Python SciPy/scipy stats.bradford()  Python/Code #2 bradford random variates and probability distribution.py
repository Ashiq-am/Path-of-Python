import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = bradford.rvs(a, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = bradford.pdf(quantile, a, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
