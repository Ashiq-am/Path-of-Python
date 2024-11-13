# import scipy.integrate
from scipy import integrate
func = lambda x: x**3

# using scipy.integrate.fixed_quad() method
gfg = integrate.fixed_quad(func, 0.0, 1.0, n = 2) # n is the order of integration

print(gfg)
