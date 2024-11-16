# import packages
import numpy as np
from numpy.polynomial import chebyshev as C

# X- coordinate
x = np.linspace(0, 1, 25)
print(x)

# y - coordinate computed from x-coordinate
y = x**3 - x**2 + np.random.randn(len(x))
print(y)

# least square fit of chebyshev series
c = C.chebfit(x, y, 2, full=False)

print('coefficients are :'+str(c))
