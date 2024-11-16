# Python code to demonstrate the
# use of numpy.cov
import numpy as np

x = [1.23, 2.12, 3.34, 4.5]

y = [2.56, 2.89, 3.76, 3.95]

# find out covariance with respect rows
cov_mat = np.stack((x, y), axis = 1)

print("shape of matrix x and y:", np.shape(cov_mat))

print("shape of covariance matrix:", np.shape(np.cov(cov_mat)))

print(np.cov(cov_mat))
