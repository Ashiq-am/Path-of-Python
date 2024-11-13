from sympy import Matrix, solve_linear_system

x, y, z = symbols('x, y, z')
A = Matrix(((1, 1, 2, 1), (1, 2, 2, 3)))
solve_linear_system(A, x, y, z)
