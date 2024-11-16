import numpy as np
from outliers import smirnov_grubbs as grubbs

# define data
data = np.array([20, 21, 26, 24, 29, 22,
				21, 50, 28, 27, 5])

print("Data after performing min one-side grubb's test: ")

# perform max Grubbs' test
grubbs.max_test(data, alpha=.05)
