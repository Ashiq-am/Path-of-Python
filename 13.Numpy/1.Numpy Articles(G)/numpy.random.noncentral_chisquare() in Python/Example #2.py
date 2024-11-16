# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using noncentral_chisquare() method
gfg = np.random.noncentral_chisquare(14.05, 3.24, 3000)

count, bins, ignored = plt.hist(gfg, 14, density = True)
plt.show()
