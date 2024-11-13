# import scipy.integrate.quad
from scipy import integrate
gfg = lambda x: x**2

# using scipy.integrate.quad() method
geek = integrate.quad(gfg, 0, 3)

print(geek)
