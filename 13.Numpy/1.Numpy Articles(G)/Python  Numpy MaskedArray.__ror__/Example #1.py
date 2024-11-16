# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([1, 2, 3, 4, 5])

# applying MaskedArray.__ror__() method
print(gfg.__ror__(2))
