# import the important module in python
import numpy as np

# make matrix with numpy
gfg = np.matrix('[4, 1; 12, 3]')

# applying matrix.setfield() method
gfg.setfield(2, np.int32)

print(gfg)
