import numpy as np

# defining the coefficients of the complex polynomial equation
coefficients = [1, 0, 1]

# finding the roots of the polynomial equation
complex_roots = np.roots(coefficients)

# printing output
print("NumPy Complex Roots:", complex_roots)
