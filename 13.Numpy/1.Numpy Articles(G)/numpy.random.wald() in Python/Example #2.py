# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using wald() method
gfg = np.random.wald(10, 5.5, 10000)

plt.hist(gfg, bins = 100, density = True)
plt.show()
