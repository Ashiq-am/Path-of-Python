# import necessary functions from scipy library
from scipy.optimize import fsolve
import numpy as np

# define the function representing the system of equations for the complex problem
def complex_equation_to_solve(z):
	return [z[0]**2 + z[1]**2 - 1, 2*z[0] + z[1] - 2]

# set an initial guess with real and imaginary parts
initial_guess = np.array([0.0, 1.0])

# use fsolve to find the root of the complex equation
complex_root = fsolve(complex_equation_to_solve, initial_guess)

# create a complex number from the obtained root
complex_solution = complex(complex_root[0], complex_root[1])

# print the result
print("SciPy Complex Solution:", complex_solution)
