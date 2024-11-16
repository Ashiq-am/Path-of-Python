import numpy as np
from numpy import linalg as geek

# Creating an array using array function
a = np.array([[1, -2j], [2j, 5]])

print("Array is:", a)

# Calculating eigenvalues and eigenvectors using eigh() function
c, d = geek.eigh(a)

print("Eigenvalues are:", c)
print("Eigenvectors are:", d)
