# Python code to demonstrate the
# use of numpy.cov
import numpy as np

x = np.array([[0, 3, 4], [1, 2, 4], [3, 4, 5]])

print("Shape of array:\n", np.shape(x))

print("Covarinace matrix of x:\n", np.cov(x))
