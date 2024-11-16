# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using power() method
gfg = np.random.power(6.75, 500)

plt.figure()
plt.hist(gfg, bins = 50, density = True)
plt.show()
