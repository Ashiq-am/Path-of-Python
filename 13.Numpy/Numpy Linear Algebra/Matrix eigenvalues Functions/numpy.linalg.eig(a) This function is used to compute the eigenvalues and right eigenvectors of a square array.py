# Python program explaining
# eig() function

from numpy import linalg as geek, np

# Creating an array using diag
# function
a = np.diag((1, 2, 3))

print("Array is :", a)

# calculating an eigen value
# using eig() function
c, d = geek.eig(a)

print("Eigen value is :", c)
print("Eigen value is :", d)