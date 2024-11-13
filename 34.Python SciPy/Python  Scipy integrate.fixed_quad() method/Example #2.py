# import scipy.integrate
from scipy import integrate
func = lambda x: x**2 + 4 * x + 4

# using scipy.integrate.fixed_quad() method
gfg = integrate.fixed_quad(func, 1.0, 2.0, n = 2) # n is the order of integration

print(gfg)
