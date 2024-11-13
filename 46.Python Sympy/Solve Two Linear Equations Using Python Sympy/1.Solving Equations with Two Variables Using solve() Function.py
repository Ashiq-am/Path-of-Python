from sympy import symbols, Eq, solve

# Define the symbolic variables
x, y = symbols('x y')

# Define the equations
eq1 = Eq(2*x + y, 5)
eq2 = Eq(x - 3*y, 7)

# Solve the equations
solution = solve((eq1, eq2), (x, y))
print(solution)
