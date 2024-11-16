# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using standard_gamma() method
gfg = np.random.standard_gamma(3.47, 5000)
gfg1 = np.random.power(gfg, 5000)

plt.hist(gfg1, bins = 50, density = True)
plt.show()
