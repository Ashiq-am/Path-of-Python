# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, [(ax1, ax2), (ax3, ax4)] = plt.subplots(2, 2)

x = np.random.randn(20, 50)
x[5, :] = 0.
x[:, 12] = 0.

ax1.spy(x, markersize = 4)
ax2.spy(x, precision = 0.2, markersize = 4)

ax3.spy(x)
ax4.spy(x, precision = 0.4)

plt.show()
ax1.set_title('matplotlib.axes.Axes.spy() Example')
plt.show()
