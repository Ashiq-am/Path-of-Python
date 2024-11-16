# import the important module in python
import numpy as np

# make matrix with numpy
gfg = np.matrix('[4, 1; 12, 3]')

# applying matrix.swapaxes() method
geek = gfg.swapaxes(0, 1)

print(geek)
