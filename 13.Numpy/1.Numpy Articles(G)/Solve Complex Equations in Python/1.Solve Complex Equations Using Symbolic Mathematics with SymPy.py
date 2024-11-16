# importing from sympy library
from sympy import symbols, Eq, solve, I

# defining the symbolic variable 'z'
z = symbols('z')

# setting up the complex equation z^2 + 1 = 0
equation = Eq(z**2 + 1, 0)

# solving the equation symbolically to find complex solutions
solutions = solve(equation, z)

# printing solutions
print("Solutions:", solutions)
