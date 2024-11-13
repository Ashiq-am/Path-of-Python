import numpy as np
quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = triang .rvs(0.158, size = 10)
print ("Random Variates : \n", R)

# PDF
x = np.linspace(0, 5, 10)
R = triang.pdf(x, 1)
print ("\nProbability Distribution : \n", R)
