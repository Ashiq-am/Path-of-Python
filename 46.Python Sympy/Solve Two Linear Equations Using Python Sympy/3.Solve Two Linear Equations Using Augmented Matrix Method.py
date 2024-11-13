from sympy import Matrix

# Define the augmented matrix
augmented_matrix = Matrix([[2, 1, 5], [1, -3, 7]])

# Solve the system
reduced_row_echelon_form = augmented_matrix.rref()[0]
solution = reduced_row_echelon_form[:, -1]
print(solution)
