# import numpy and scipy.integrate
import numpy as np
from scipy import integrate

x = np.arange(0, 10)
y = np.sqrt(x)
# using scipy.integrate.simps() method
gfg = integrate.simps(y, x)

print(gfg)
