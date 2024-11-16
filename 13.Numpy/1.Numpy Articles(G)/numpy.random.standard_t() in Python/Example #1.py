# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using standard_t() method
gfg = np.random.standard_t(5, 5000)

plt.hist(gfg, bins = 50, density = True)
plt.show()
