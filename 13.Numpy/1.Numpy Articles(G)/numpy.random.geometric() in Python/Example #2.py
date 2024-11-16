# import numpy and geometric
import numpy as np
import matplotlib.pyplot as plt

# Using geometric() method
gfg = np.random.geometric(0.85, 1000)

count, bins, ignored = plt.hist(gfg, 10, density = True)
plt.show()
