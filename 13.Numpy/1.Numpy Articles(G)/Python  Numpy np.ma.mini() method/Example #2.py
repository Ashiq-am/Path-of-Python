# import numpy
import numpy as np
import numpy.ma as ma

# using np.ma.mini() method
gfg = ma.array(np.arange(10), mask =[-2, -1, 0, 1, 0, 3, 0, 0, 0, 0]).reshape(2, 5)
min = gfg.mini()

print(min)
