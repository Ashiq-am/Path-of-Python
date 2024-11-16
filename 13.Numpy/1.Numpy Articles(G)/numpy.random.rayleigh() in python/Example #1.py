# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using rayleigh() method
gfg = np.random.rayleigh(3.4, 50000)

plt.figure()
plt.hist(gfg, bins = 50, density = True)
plt.show()
