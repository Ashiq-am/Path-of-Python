# import choice
import numpy as np
import matplotlib.pyplot as plt

# Using choice() method
gfg = np.random.choice(5, 1000, p =[0.2, 0.1, 0.3, 0.4, 0])

count, bins, ignored = plt.hist(gfg, 14, density = True)
plt.show()
