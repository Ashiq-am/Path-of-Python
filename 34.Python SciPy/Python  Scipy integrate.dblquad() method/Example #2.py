# import scipy.integrate.dblquad
from scipy import integrate
gfg = lambda y, x: x * y**2 + 2 * x*y + 4

# using scipy.integrate.dblquad() method
geek = integrate.dblquad(gfg, 1, 4, lambda x: 0, lambda x: 1)

print(geek)
