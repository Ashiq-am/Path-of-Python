# import dirichlet
import numpy as np
import matplotlib.pyplot as plt

# Using dirichlet() method
gfg = np.random.dirichlet((6, 5, 4, 3, 2, 1), 1000)

count, bins, ignored = plt.hist(gfg, 30, density = True)
plt.show()
