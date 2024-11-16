# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.array([[1.1, 2, 3.3, 4, 5],
                [6, 5.2, 4, 3, 2.2]])

# applying ndarray.__array__() method
geeks = gfg.__array__(int)

print(geeks)
