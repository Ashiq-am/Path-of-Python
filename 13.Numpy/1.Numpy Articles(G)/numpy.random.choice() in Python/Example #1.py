# import choice
import numpy as np
import matplotlib.pyplot as plt

# Using choice() method
gfg = np.random.choice(13, 5000)

count, bins, ignored = plt.hist(gfg, 25, density = True)
plt.show()
