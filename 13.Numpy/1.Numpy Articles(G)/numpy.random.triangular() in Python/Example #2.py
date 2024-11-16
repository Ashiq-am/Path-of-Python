# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using triangular() method
gfg = np.random.triangular(-10, 8, 10, 15000)

plt.hist(gfg, bins = 100, density = True)
plt.show()
