# Import the required libraries
from scipy import linalg
import numpy as np

# Initializing the matrix
x = np.array([[8 , 2] , [3 , 5] , [1 , 3]])

# finding the pseudo inverse of matrix x
y = linalg.pinv(x)
print(y)
