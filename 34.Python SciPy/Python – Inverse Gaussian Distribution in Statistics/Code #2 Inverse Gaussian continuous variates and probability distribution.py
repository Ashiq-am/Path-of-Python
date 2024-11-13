import numpy as np

quantile = np.arange(0.01, 1)

# Random Variates
R = invgauss.ppf(0.01, a)
print("Random Variates : \n", R)

# PDF
R = invgauss.pdf(invgauss.ppf(0.01, a), a)
print("\nProbability Distribution : \n", R)
