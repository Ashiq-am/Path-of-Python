# Python program to display variance
# of data groups

# Import library
import scipy.stats as stats
import numpy as np

# Creating data groups
data_group1 = np.array([14, 15, 15, 16, 13, 8, 14,
						17, 16, 14, 19, 20, 21, 15,
						15])
data_group2 = np.array([36, 37, 44, 27, 24, 28, 27,
						39, 29, 24, 37, 32, 24, 26,
						33])

# Print the variance of both data groups
print(np.var(data_group1), np.var(data_group2))
