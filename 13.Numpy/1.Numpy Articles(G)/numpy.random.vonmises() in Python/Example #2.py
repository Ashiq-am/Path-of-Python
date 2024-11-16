# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using vonmises() method
gfg = np.random.vonmises(5, 13, 10000)

plt.hist(gfg, bins = 100, density = True)
plt.show()
