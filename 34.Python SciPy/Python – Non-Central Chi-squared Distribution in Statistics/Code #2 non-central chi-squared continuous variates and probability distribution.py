import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = ncx2.rvs(a, b)
print ("Random Variates : \n", R)

# PDF
R = ncx2.pdf(a, b, quantile)
print ("\nProbability Distribution : \n", R)
