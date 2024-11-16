# Python Program illustrating
# numpy.outer() method
import numpy as np

# Vectors
a = np.array([2, 6])
b = np.array([3, 10])
print("Vectors :")
print("a = ", a)
print("\nb = ", b)

# Outer product of vectors
print("\nOuter product of vectors a and b =")
print(np.outer(a, b))

print("------------------------------------")

# Matrices
x = np.array([[3, 6, 4], [9, 4, 6]])
y = np.array([[1, 15, 7], [3, 10, 8]])
print("\nMatrices :")
print("x =", x)
print("\ny =", y)

# Outer product of matrices
print("\nOuter product of matrices x and y =")
print(np.outer(x, y))
