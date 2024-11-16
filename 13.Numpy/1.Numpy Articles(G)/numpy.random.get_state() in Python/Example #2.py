# import numpy and get_state
import numpy as np
import matplotlib.pyplot as plt

# Using get_state() method
gfg = np.random.get_state()[1]

count, bins, ignored = plt.hist(gfg, 24, density = True)
plt.show()
