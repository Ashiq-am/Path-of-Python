# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([[10, 20, 30, 40, 50],
				[110, 220, 330, 440, 550]])

# applying MaskedArray.__rtruediv__() method
print(gfg.__rtruediv__(10))
