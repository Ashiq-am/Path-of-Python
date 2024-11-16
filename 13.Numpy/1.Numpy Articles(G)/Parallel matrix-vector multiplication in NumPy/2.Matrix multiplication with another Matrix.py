import numpy as np

a = np.array([[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]])

b = np.array([[11, 22, 33],
			[44, 55, 66],
			[77, 88, 99]])

print("Matrix a =", a)
print("Matrix b =", b)
print("Product of a and b =", np.matmul(a, b))
