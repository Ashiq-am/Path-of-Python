# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using rayleigh() method
gfg = np.random.rayleigh(2 * np.sqrt(np.pi), 100000)

plt.figure()
plt.hist(gfg, bins = 50, density = True)
plt.show()
