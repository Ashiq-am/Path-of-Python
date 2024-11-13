# import scipy.integrate.
from scipy import integrate

gfg = lambda x: x**2 + 2 * x + 4

# using scipy.integrate.quadrature() method
geek = integrate.quadrature(gfg, 0.0, 4.0)

print(geek)
