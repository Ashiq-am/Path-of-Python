# Implementation of matplotlib.pyplot.ylabels()
# function

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-180.0, 180.0, 0.1)
s = np.radians(t) / 2.

plt.plot(t, s, '-', lw=2)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('ylabels() function')
plt.grid(True)

plt.show()
