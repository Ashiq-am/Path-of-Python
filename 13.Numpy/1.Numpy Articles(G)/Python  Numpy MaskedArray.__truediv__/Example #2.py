# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([[10, 20, 30, 40, 50],
				[11, 22, 33, 44, 55]])

# applying MaskedArray.__truediv__() method
print(gfg.__truediv__(5))
