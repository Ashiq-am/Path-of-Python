import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = kstwobign.rvs(a, b, scale = 2, size = 10)
print ("Random Variates : \n", R)
