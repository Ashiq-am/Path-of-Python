import matplotlib.pyplot as plot
import numpy as np

# an array with linearly increasing values
array = np.diag(range(20))

plot.matshow(array)

plot.show()
