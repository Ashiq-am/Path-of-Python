# import numpy and scipy.integrate
import numpy as np
from scipy import integrate
x = np.arange(3, 12)
y = np.cos(np.power(x, 3.5))

# using scipy.integrate.romb() method
gfg = integrate.romb(y)

print(gfg)
