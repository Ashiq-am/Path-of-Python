# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

n = 100000
x = np.random.standard_normal(n)
y = 2 * np.random.standard_normal(n)
z = [1, 2, 3, 4]
xmin = x.min()
xmax = x.max()
ymin = y.min()
ymax = y.max()

hb = plt.hexbin(x, y, gridsize=50,
                bins=z, cmap='BuGn')

plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

cb = plt.colorbar(hb)
cb.set_label(z)
plt.title('matplotlib.pyplot.hexbin()\
Example')

plt.show()
