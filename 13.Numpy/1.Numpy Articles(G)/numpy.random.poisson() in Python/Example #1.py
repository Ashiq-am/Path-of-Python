# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using poisson() method
gfg = np.random.poisson(10, 1000)

count, bins, ignored = plt.hist(gfg, 14, density = True)
plt.show()
