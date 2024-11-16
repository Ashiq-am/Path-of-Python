import numpy as np
from numpy import linalg as geek

# Creating an array using diag function
a = np.diag((1, 2, 3))

print("Array is:", a)

# Calculating eigenvalues and eigenvectors using eig() function
c, d = geek.eig(a)

print("Eigenvalues are:", c)
print("Eigenvectors are:", d)
