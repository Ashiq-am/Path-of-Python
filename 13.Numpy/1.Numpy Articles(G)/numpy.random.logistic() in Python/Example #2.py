# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using numpy.random.logistic() method
gfg = np.random.logistic(13.31, 3.31, 1000)

count, bins, ignored = plt.hist(gfg, 30, density = True)
plt.show()
