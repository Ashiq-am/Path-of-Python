# import numpy and scipy.integrate
import numpy as np
from scipy import integrate

f = lambda x: 3*(np.pi)*x**3

# using scipy.integrate.romberg()
g = integrate.romberg(f, 1, 2, show = True)

print(g)
