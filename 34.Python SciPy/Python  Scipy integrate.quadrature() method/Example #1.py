# import scipy.integrate.
from scipy import integrate

gfg = lambda x: x**8 + x**4

# using scipy.integrate.quadrature() method
geek = integrate.quadrature(gfg, 0.0, 1.8)

print(geek)
