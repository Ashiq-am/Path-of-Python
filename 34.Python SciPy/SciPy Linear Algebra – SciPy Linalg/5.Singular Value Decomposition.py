# Importing the required libraries
from scipy import linalg
import numpy as np

# Initializing the matrix M
M = np.array([[1 , 5] , [6 , 10]])

# Passing the values to the
# eigen function
x , y , z = linalg.svd(M)
print(x , y , z)
