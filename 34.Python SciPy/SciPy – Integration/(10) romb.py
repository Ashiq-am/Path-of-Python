# import numpy and scipy.integrate
import numpy as np
from scipy import integrate


x = np.arange(0,5)

# using scipy.integrate.romb() method
f = integrate.romb(x)

print(f)
