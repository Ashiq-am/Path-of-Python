# import numpy
import numpy as np

# initialize 2d vectors
a = np.array([[3, 9],
              [2, 5]])
b = np.array([[6, 1],
              [4, 8]])

# Checking the condition "No. of columns
# of first vector == No. of rows of the
# second vector"
if a.shape[1] == b.shape[0]:

    # calculating Dot product using np.dot
    c = np.dot(a, b)
    print("Dot product of a and b is:\n", c)
else:
    print("No. of columns of first vector should match\
	with No. of rows of the second vector")
