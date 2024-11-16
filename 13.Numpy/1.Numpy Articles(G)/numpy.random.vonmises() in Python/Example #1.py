# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using vonmises() method
gfg = np.random.vonmises(5, 3, 5000)

plt.hist(gfg, bins = 50, density = True)
plt.show()
