# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using weibull() method
gfg = np.random.weibull(6.78, 10000)

plt.hist(gfg, bins = 100, density = True)
plt.show()
