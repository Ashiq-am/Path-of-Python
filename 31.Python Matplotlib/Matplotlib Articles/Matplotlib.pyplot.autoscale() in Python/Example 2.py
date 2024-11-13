import numpy as np
import matplotlib.pyplot as plt


x, y = np.arange(0, 101, 1), 300 - 0.1 * np.arange(0, 101, 1)
mask = (x >= 50) & (x <= 100)

fig, ax = plt.subplots()
ax.scatter(x[mask], y[mask])

plt.autoscale()
plt.show()
