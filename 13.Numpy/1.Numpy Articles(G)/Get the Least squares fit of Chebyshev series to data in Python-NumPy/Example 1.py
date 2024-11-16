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
c, stats = C.chebfit(x, y, 2, full=True)

print('coefficients are :'+str(c))
print('residuals '+str(stats[0]))
print('rank :'+str(stats[1]))
print('singular_values :'+str(stats[2]))
print('rcond: '+str(stats[3]))
