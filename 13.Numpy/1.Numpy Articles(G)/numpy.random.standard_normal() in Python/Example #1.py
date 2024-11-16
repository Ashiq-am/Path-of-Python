# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using standard_normal() method
gfg = np.random.standard_normal(5000)

plt.hist(gfg, bins = 50, density = True)
plt.show()
