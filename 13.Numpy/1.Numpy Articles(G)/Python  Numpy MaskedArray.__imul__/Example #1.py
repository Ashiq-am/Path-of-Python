# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([1, 2, 3, 4.7, 5.2])

# applying MaskedArray.__imul__() method
print(gfg.__imul__(5))
