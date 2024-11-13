# import scipy.integrate.quad
from scipy import integrate
gfg = lambda x: x**2 + x + 1

# using scipy.integrate.quad() method
geek = integrate.quad(gfg, 1, 4)

print(geek)
