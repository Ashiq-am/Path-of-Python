# import numpy and f
import numpy as np
import matplotlib.pyplot as plt

# Using f() method
gfg = np.random.f(14.56, 31.45, 30000)
gfg1 = np.random.f(gfg, 10.45, 30000)

count, bins, ignored = plt.hist(gfg1, 14, density = True)
plt.show()
