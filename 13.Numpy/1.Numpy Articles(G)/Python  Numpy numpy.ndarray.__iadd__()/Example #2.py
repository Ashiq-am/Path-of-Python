# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.array([[1, 2.2, 3, 4, 5.01],
                [6.1, 5, 4.8, 3, 2]])

# applying ndarray.__iadd__() method
print(gfg.__iadd__(3))
