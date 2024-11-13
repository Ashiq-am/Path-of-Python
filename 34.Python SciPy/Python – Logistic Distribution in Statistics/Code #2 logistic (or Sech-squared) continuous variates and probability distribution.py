import numpy as np
quantile = np.arange (0.03, 2, 0.21)

# Random Variates
R = logistic.rvs(a, b)
print ("Random Variates : \n", R)

# PDF
R = logistic.pdf(a, b, quantile)
print ("\nProbability Distribution : \n", R)
