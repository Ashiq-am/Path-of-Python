# import scipy.integrate.tplquad
from scipy import integrate

gfg = lambda z, y, x: x * y*z + x**2 + y**2 + z**2

# using scipy.integrate.tplquad() method
geek = integrate.tplquad(gfg, 1, 3, lambda x: 2, lambda x: 3,
							lambda x, y: 0, lambda x, y: 1)

print(geek)
