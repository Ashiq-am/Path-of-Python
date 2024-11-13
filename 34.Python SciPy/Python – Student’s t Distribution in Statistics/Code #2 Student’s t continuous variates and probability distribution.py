import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = t.rvs(a, b)
print ("Random Variates : \n", R)

# PDF
R = t.pdf(a, b, quantile)
print ("\nProbability Distribution : \n", R)
