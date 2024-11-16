# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using standard_exponential() method
gfg = np.random.standard_exponential(5000)

plt.hist(gfg, bins = 50, density = True)
plt.show()
