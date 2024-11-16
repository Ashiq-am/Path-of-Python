# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using permutation() method
gfg = np.random.permutation(200)

count, bins, ignored = plt.hist(gfg, 14, density = True)
plt.show()
