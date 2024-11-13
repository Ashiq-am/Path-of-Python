# import scipy.integrate
from scipy import integrate


def func(x): return 3*x**3


# using scipy.integrate.fixed_quad() method
# n is the order of integration
gfg = integrate.fixed_quad(func, 1.0, 2.0, n=2)

print(gfg)
