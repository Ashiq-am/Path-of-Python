# import numpy
import numpy as np
import matplotlib.pyplot as plt

# Using standard_cauchy() method
gfg = np.random.standard_cauchy(100000)

gfg = gfg[(gfg>-25) & (gfg<25)]
plt.hist(gfg, bins = 100, density = True)
plt.show()
