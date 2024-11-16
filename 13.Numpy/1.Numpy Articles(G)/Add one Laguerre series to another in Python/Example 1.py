import numpy as np
import numpy.polynomial.laguerre as geeks

# Laguerre series coefficients
series1 = (10, 20, 30, 40, 50)
series2 = (1, 2, 3, 4, 5)

# using np.lagadd() method
result = geeks.lagadd(series1, series2)

# Resulting laguerre series
print(result)
