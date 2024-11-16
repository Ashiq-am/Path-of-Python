# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using standard_exponential() method
gfg = np.random.standard_exponential(10000)

plt.hist(gfg, bins = 100, density = True)
plt.show()
