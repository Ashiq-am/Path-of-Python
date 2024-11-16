# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([1, 2.5, 3, 7, 5])

# applying MaskedArray.__imod__() method
print(gfg.__imod__(2))
