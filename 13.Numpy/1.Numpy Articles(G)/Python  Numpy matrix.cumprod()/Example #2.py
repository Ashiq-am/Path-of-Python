# import the important module in python
import numpy as np

# make a matrix with numpy
gfg = np.matrix('[1, 2, 3; 4, 5, 6]')

# applying matrix.cumprod() method
geeks = gfg.cumprod()

print(geeks)
