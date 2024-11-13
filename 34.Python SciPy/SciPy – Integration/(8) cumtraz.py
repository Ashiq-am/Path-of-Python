# import numpy and scipy.integrate.cumtrapz
import numpy as np
from scipy import integrate

a = np.arange(0, 5)
b = np.arange(0, 5)

# using scipy.integrate.cumtrapz() method
f = integrate.cumtrapz(b, a)

print(f)
