# import numpy and lagtrim
import numpy as np
from numpy.polynomial.laguerre import lagtrim

# using np.lagtrim() method
gfg = lagtrim([1, 2, 3, 0, 0], 0)

print(gfg)
