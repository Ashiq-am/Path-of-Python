# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using numpy.random.pareto() method
gfg = np.random.pareto(13.89, 1000)

count, bins, ignored = plt.hist(gfg, 14, density = True)
plt.show()
