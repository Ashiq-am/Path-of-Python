import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = nct.rvs(a, b, c)
print ("Random Variates : \n", R)

# PDF
R = nct.pdf(a, b, c, quantile)
print ("\nProbability Distribution : \n", R)
