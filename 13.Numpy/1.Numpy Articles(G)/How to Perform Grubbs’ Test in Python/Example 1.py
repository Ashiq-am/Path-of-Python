import numpy as np
from outliers import smirnov_grubbs as grubbs

# define data
data = np.array([20, 21, 26, 24, 29, 22,
				21, 50, 28, 27])

# perform Grubbs' test
grubbs.test(data, alpha=.05)
