import numpy as np


# Array formation
a = np.arange(10)

# Cumulative sum of array, column wise,
# float datatype
c = np.add.accumulate(a, axis = 0, dtype = float)

print("The array {0} gets added cumulatively to {1}".format(a, c))
