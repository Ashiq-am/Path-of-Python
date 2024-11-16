# import dirichlet
import numpy as np
import matplotlib.pyplot as plt

# Using dirichlet() method
gfg = np.random.dirichlet((3, 4, 5, 19), size = 1000)

count, bins, ignored = plt.hist(gfg, 30, density = True)
plt.show()
