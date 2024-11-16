# Python Program illustrating
# numpy.cross() method
import numpy as np

# Vectors
a = np.array([3, 6])
b = np.array([9, 10])
print("Vectors :")
print("a = ", a)
print("\nb = ", b)

# Cross product of vectors
print("\nCross product of vectors a and b =")
print(np.cross(a, b))

print("------------------------------------")

# Matrices
x = np.array([[2, 6, 9], [2, 7, 3]])
y = np.array([[7, 5, 6], [3, 12, 3]])
print("\nMatrices :")
print("x =", x)
print("\ny =", y)

# Cross product of matrices
print("\nCross product of matrices x and y =")
print(np.cross(x, y))
