# import chisquare
import numpy as np
import matplotlib.pyplot as plt

# Using chisquare() method
gfg = np.random.chisquare(3, 1000)

count, bins, ignored = plt.hist(gfg, 14, density = True)
plt.show()
