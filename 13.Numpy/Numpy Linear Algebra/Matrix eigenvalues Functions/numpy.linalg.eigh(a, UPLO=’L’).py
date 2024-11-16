# Python program explaining
# eigh() function

from numpy import linalg as geek, np

# Creating an array using array
# function
a = np.array([[1, -2j], [2j, 5]])

print("Array is :", a)

# calculating an eigen value
# using eigh() function
c, d = geek.eigh(a)

print("Eigen value is :", c)
print("Eigen value is :", d)