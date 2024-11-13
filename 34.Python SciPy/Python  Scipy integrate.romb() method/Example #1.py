# import numpy and scipy.integrate
import numpy as np
from scipy import integrate
x = np.arange(3, 12)

# using scipy.integrate.romb() method
gfg = integrate.romb(x)

print(gfg)
