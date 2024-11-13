# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

plt.ioff()
plt.plot([1.4, 2.5, 0.3])

axes = plt.gca()
axes.plot([3.1, 2.2, 6])

plt.title('matplotlib.pyplot.ioff() function Example',
          fontweight="bold")

plt.show()
