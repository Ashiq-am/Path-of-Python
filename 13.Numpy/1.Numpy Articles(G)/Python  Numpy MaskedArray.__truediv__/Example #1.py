# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([22, 33.7, 44.5, 55, 77])

# applying MaskedArray.__truediv__() method
print(gfg.__truediv__(11))
