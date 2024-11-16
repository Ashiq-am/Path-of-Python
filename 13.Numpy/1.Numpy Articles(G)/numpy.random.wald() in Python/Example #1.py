# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using wald() method
gfg = np.random.wald(5, 3.7, 5000)

plt.hist(gfg, bins = 50, density = True)
plt.show()
