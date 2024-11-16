# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using standard_cauchy() method
gfg = np.random.standard_cauchy(100000)
gfg1 = np.random.power([gfg>0], 100000)

plt.hist(gfg1, bins = 100, density = True)
plt.show()
