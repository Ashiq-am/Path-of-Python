import numpy as np
import numpy as np
from scipy.stats import gilbrat

quantile = np.arange (0.01, 1, 0.1)

# Random Variates
R = gilbrat.rvs(scale = 2, size = 10)
print ("Random Variates : \n", R)

# PDF
R = gilbrat.pdf(quantile, loc = 0, scale = 1)
print ("\nProbability Distribution : \n", R)
