# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.ma.array([[10, 20, 30, 4.45, 50],
                   [6, 5.5, 4, 3, 2.62]])

# applying MaskedArray.__ifloordiv__() method
print(gfg.__ifloordiv__(5))
