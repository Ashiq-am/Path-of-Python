# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([[14, 22, 31, 47, 54],
                   [64, 53.5, 44, 36, 21]])

# applying MaskedArray.__imod__() method
print(gfg.__imod__(5))
