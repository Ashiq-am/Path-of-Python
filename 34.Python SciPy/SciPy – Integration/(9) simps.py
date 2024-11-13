# import numpy and scipy.integrate
import numpy as np
from scipy import integrate

a = np.arange(0, 5)
b = np.arange(0, 5)

# using scipy.integrate.simps() method
f = integrate.simps(b, a)

print(f)
