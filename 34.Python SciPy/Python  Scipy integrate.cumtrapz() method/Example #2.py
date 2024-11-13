# import numpy and scipy.integrate.cumtrapz
import numpy as np
from scipy import integrate

x = np.arange(0, 10)
y = np.power(x, 2)
# using scipy.integrate.cumtrapz() method
gfg = integrate.cumtrapz(y, x)

print(gfg)
