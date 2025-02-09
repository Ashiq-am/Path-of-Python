# Creating a square matrix
matrix = np.array([[4, 2], [3, 1]])

# Calculating the determinant
determinant = np.linalg.det(matrix)
print("Determinant:", determinant)

# Calculating the inverse
inverse_matrix = np.linalg.inv(matrix)
print("Inverse Matrix:\n", inverse_matrix)