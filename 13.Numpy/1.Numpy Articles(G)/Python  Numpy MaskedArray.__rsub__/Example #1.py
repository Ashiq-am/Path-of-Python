# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([11, 22, 23, 24, 25])

# applying MaskedArray.__rsub__() method
print(gfg.__rsub__(5))
