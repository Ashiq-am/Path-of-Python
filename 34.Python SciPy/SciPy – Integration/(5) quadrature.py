# import scipy.integrate.
from scipy import integrate

def f(x): return 3*x**3

# using scipy.integrate.quadrature() method
g = integrate.quadrature(f, 0.0, 1.0)

print(g)
