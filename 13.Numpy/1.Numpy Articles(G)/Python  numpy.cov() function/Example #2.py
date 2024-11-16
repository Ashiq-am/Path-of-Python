# Python code to demonstrate the
# use of numpy.cov
import numpy as np

x = [1.23, 2.12, 3.34, 4.5]

y = [2.56, 2.89, 3.76, 3.95]

# find out covariance with respect columns
cov_mat = np.stack((x, y), axis = 0)

print(np.cov(cov_mat))
