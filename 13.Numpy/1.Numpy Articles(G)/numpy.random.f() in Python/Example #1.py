# import numpy and f
import numpy as np
import matplotlib.pyplot as plt

# Using f() method
gfg = np.random.f(0.98, 15.43, 1000)

count, bins, ignored = plt.hist(gfg, 30, density = True)
plt.show()
