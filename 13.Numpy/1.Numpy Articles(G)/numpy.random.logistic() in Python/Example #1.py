# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using numpy.random.logistic() method
gfg1 = np.random.logistic(1.23, 3.14, 1000)
gfg2 = np.random.logistic(gfg1, 3.14, 1000)

count, bins, ignored = plt.hist(gfg2, 50, density = True)
plt.show()
