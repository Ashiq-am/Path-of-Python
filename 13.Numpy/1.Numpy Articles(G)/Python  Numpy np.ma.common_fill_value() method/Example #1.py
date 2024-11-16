# import numpy
import numpy as np

x = np.ma.array([1, 2, 3], fill_value = 1)
y = np.ma.array([7, 8, 9], fill_value = 1)

# using np.ma.common_fill_value() method
gfg = np.ma.common_fill_value(x, y)

print(gfg)
