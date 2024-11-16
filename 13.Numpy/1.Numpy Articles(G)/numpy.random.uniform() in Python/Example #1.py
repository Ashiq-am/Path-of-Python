# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using uniform() method
gfg = np.random.uniform(-5, 5, 5000)

plt.hist(gfg, bins = 50, density = True)
plt.show()
