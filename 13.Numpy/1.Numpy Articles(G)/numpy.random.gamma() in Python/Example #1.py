# import numpy and gamma
import numpy as np
import matplotlib.pyplot as plt

# Using gamma() method
gfg = np.random.gamma(3, 20, 1000)

count, bins, ignored = plt.hist(gfg, 14, density = True)
plt.show()
