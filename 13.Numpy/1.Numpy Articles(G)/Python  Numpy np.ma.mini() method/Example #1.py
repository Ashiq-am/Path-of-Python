# import numpy
import numpy as np
import numpy.ma as ma

# using np.ma.mini() method
gfg = ma.array(np.arange(6), mask =[-2, -1, 0, 1, 2, 3]).reshape(3, 2)
min = gfg.mini()

print(min)
