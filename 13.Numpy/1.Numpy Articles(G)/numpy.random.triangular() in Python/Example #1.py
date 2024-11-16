# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using triangular() method
gfg = np.random.triangular(-5, 0, 5, 5000)

plt.hist(gfg, bins = 50, density = True)
plt.show()
