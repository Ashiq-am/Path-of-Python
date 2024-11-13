# Import the required libraries
from scipy import linalg
import numpy as np

# Initializing the matrix
x = np.array([[7, 2], [4, 5]])

# Finding the inverse of
# matrix x
y = linalg.inv(x)
print(y)
