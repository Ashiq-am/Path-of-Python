# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using noncentral_f() method
gfg = np.random.noncentral_f(10.23, 12.13, 3, 10000)

count, bins, ignored = plt.hist(gfg, 14, density = True)
plt.show()
