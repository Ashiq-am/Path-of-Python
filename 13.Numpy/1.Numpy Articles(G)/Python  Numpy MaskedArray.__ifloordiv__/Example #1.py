# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([10, 20.5, 30, 4.8, 50])

# applying MaskedArray.__ifloordiv__() method
print(gfg.__ifloordiv__(2))
