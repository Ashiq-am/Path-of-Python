# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using weibull() method
gfg = np.random.weibull(5, 5000)

plt.hist(gfg, bins = 50, density = True)
plt.show()
