# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using noncentral_f() method
gfg = np.random.noncentral_f(1.24, 21, 3, 1000)

count, bins, ignored = plt.hist(gfg, 50, density = True)
plt.show()
