# import numpy and gamma
import numpy as np
import matplotlib.pyplot as plt

# Using gamma() method
gfg = np.random.gamma(4.98, 12, 40000)
gfg1 = np.random.gamma(gfg, 13.46, 40000)

count, bins, ignored = plt.hist(gfg1, 50, density = True)
plt.show()
