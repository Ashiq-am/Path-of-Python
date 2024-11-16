# import numpy
import numpy as np

x = np.ma.array([[1, 2], [2, 1]], fill_value = 2)
y = np.ma.array([[1, 5], [5, 1]], fill_value = 5)

# using np.ma.common_fill_value() method
gfg = np.ma.common_fill_value(x, y)

print(gfg)
