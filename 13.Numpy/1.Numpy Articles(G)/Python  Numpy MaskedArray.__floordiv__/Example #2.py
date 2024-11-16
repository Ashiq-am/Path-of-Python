# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([[1, 2, 3, 4.45, 5],
				[6, 5.5, 4, 3, 2.62]])

# applying MaskedArray.__floordiv__() method
print(gfg.__floordiv__(3))
