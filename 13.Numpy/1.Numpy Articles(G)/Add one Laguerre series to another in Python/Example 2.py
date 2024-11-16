import numpy as np
import numpy.polynomial.laguerre as geeks

# Laguerre series coefficients
series1 = (8, 7, 6, 5)
series2 = (2, 3, 4, 5)

# using np.lagadd() method
result = geeks.lagadd(series1, series2)

# Resulting laguerre series
print(result)
