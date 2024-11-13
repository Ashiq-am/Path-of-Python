# Importing the required libraries
from scipy import linalg
import numpy as np

# Initializing the matrix A
A = np.array([[9 , 6] , [4 , 5]])

# Finding the determinant of matrix A
D = linalg.det(A)
print(D)
