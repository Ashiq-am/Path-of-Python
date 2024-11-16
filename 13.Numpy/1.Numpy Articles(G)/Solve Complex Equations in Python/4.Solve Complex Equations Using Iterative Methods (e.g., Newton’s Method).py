import numpy as np

# defining the complex equation to solve
def complex_equation_to_solve(z):
	return z**2 + 1

# defining the derivative of the equation for Newton's method
def complex_equation_derivative(z):
	return 2 * z

# setting an initial guess with a complex number
initial_guess = complex(0.0, 1.0)

# setting the maximum number of iterations
max_iterations = 100

# Newton's method iteratively
for _ in range(max_iterations):
	initial_guess -= complex_equation_to_solve(
		initial_guess) / complex_equation_derivative(initial_guess)

complex_solution = initial_guess

# printing output
print("Newton's Method Complex Solution:", complex_solution)
