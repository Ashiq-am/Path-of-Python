# import numpy and scipy.integrate
import numpy as np
from scipy import integrate
gfg = lambda x: np.exp(-x**2) + 1 / np.sqrt(np.pi)

# using scipy.integrate.romberg()
geek = integrate.romberg(gfg, 1, 2, show = True)

print(geek)
