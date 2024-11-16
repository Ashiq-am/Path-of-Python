# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using noncentral_chisquare() method
gfg = np.random.noncentral_chisquare(1.21, 9.89, 1000)

count, bins, ignored = plt.hist(gfg, 30, density = True)
plt.show()
