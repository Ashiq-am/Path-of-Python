# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([[21, 22, 23, 24, 25],
				[26, 25, 24, 23, 22]])

# applying MaskedArray.__sub__() method
print(gfg.__sub__(5))
