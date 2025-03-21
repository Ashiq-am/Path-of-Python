# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 200, 10)
yy = np.transpose([2 * np.sin(x + phi) for phi in x])

fig, ax = plt.subplots()
ax.plot(yy)
w = ax.invert_yaxis()
ax.set_title('matplotlib.axes.Axes.invert_yaxis()\
Example', fontsize=14, fontweight='bold')
plt.show()
