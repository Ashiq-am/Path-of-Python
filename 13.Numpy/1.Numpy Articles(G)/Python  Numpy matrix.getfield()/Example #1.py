# import the important module in python
import numpy as np

# make matrix with numpy
gfg = np.matrix('[6, 1; 2, 3]')

# applying matrix.getfield() method
geeks = gfg.getfield(int)

print(geeks)
