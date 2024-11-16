# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using numpy.random.laplace() method
gfg = np.random.laplace(0.5, 12.45, 1000)
gfg1 = np.random.laplace(gfg, 12.45, 1000)

count, bins, ignored = plt.hist(gfg1, 40, density = True)
plt.show()
