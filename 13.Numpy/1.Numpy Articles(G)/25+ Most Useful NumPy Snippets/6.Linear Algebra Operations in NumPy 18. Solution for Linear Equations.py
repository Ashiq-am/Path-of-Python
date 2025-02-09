# Coefficient matrix A
A = np.array([[3, 2], [1, 2]])

# Constant matrix b
b = np.array([5, 5])

# Solving for x in Ax = b
solution = np.linalg.solve(A, b)
print("Solution to the linear equations:\n", solution)