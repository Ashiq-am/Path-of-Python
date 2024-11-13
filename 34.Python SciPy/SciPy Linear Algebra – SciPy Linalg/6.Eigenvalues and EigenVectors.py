# Importing the required libraries
from scipy import linalg
import numpy as np

# Initializing the matrix M
M = np.array([[9 , 3] , [2 , 4]])

# Passing the values to the eigen
# function
val , vect = linalg.eig(M)

# Display the Eigen values and Eigen
# vectors
print(val)
print(vect)
