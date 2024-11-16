# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.array([[1, 2, 3, 4, 5],
                [6, 5, 4, 3, 2]])

# applying ndarray.__copy__() method
geeks = gfg.__copy__()

# Change the data element
geeks[0][2] = 10

print(gfg, end='\n\n')
print(geeks)
