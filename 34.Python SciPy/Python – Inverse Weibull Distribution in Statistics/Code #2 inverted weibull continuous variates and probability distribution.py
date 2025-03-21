import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = invweibull.rvs(a, scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = invweibull.pdf(a, quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
