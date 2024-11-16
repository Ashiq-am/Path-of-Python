# import numpy
import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(12).reshape((4, 3))
# Using permutation() method
gfg = np.random.permutation(arr)

count, bins, ignored = plt.hist(gfg, 14, density = True)
plt.show()
