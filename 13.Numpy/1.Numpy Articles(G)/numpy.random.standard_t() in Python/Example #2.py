# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using standard_t() method
gfg = np.random.standard_t(7, 10000)

plt.hist(gfg, bins = 50, density = True)
plt.show()
