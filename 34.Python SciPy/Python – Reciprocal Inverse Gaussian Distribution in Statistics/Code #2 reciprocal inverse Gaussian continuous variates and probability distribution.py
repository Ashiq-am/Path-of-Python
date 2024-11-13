import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = recipinvgauss .rvs(a, b)
print ("Random Variates : \n", R)

# PDF
R = recipinvgauss .pdf(a, b, quantile)
print ("\nProbability Distribution : \n", R)
