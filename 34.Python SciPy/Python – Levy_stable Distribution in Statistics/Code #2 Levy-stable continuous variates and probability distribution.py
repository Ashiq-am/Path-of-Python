import numpy as np
quantile = np.arange (0.03, 2, 0.21)

# Random Variates
R = levy_stable.rvs(1.8, -0.5, size = 10)
print ("Random Variates : \n", R)

# PDF
R = levy_stable.pdf(a, b, quantile)
print ("\nProbability Distribution : \n", R)
