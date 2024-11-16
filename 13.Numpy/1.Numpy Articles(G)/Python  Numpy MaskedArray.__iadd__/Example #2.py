# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([[1, 2, 3, 4, 5],
				[6, 5, 4, 3, 2]])

# applying MaskedArray.__iadd__() method
print(gfg.__iadd__(5))
