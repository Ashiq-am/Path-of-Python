# import scipy.integrate.dblquad
from scipy import integrate

gfg = lambda y, x: x * y**2

# using scipy.integrate.dblquad() method
geek = integrate.dblquad(gfg, 0, 3, lambda x: 0, lambda x: 1)

print(geek)
