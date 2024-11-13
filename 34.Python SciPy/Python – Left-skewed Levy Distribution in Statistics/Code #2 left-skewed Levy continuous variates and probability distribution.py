import numpy as np
quantile = np.arange (0.03, 2, 0.21)

# Random Variates
R = levy_l.rvs(a, b)
print ("Random Variates : \n", R)

# PDF
R = levy_l.pdf(a, b, quantile)
print ("\nProbability Distribution : \n", R)
