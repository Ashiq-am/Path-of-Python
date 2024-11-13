# import numpy and scipy.integrate
import numpy as np
from scipy import integrate
gfg = lambda x: np.exp(-x**2)

# using scipy.integrate.romberg()
geek = integrate.romberg(gfg, 0, 3, show = True)

print(geek)
