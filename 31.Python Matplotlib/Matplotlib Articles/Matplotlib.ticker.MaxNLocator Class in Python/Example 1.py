import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np


N = 10
x = np.arange(N)
y = np.random.randn(N)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)

# Create your ticker object with M ticks
M = 3
yticks = ticker.MaxNLocator(M)

# Set the yaxis major locator using
# your ticker object.
ax.yaxis.set_major_locator(yticks)

plt.show()
