# import exponential
import numpy as np
import matplotlib.pyplot as plt

# Using exponential() method
gfg = np.random.exponential(3.45, 10000)

count, bins, ignored = plt.hist(gfg, 14, density = True)
plt.show()
