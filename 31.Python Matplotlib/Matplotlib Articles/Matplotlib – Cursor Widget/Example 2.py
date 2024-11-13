# Import MultiCursor from matplotlib
from matplotlib.widgets import MultiCursor
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.sin(x)
z = np.cos(x)

ax1.plot(x, y, label="sin function")
ax1.legend(loc="upper right")
ax2.plot(x, z, label="cos function")

multi = MultiCursor(fig.canvas, (ax1, ax2), color='g', lw=2,
					horizOn=False, vertOn=True)

ax2.legend(loc="upper right")
plt.show()
