import numpy as np
from scipy.stats import halfgennorm

quantile = np.arange(0.01, 1, 0.1)

# Random Variates
R = halfgennorm.rvs(.2, scale=2, size=10)
print("Random Variates : \n", R)

# PDF
R = halfgennorm.pdf(quantile, .2, loc=0, scale=1)
print("\nProbability Distribution : \n", R)
