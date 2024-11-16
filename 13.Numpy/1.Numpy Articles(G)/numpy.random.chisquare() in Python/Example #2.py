# import chisquare
import numpy as np
import matplotlib.pyplot as plt

# Using chisquare() method
gfg = np.random.chisquare(5, 10000)
gfg1 = np.random.chisquare(gfg, 10000)

count, bins, ignored = plt.hist(gfg1, 30, density = True)
plt.show()
