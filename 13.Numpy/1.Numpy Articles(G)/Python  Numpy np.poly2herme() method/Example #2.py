# import numpy and poly2herme
import numpy as np
from numpy.polynomial.hermite_e import poly2herme

x = np.array([-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.4, 0.5])
# using np.poly2herme() method
gfg = poly2herme(x)

print(gfg)
