import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)

fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_ylim(1, 0)
ax.set_ylabel('Display Y-axis Label',
			fontweight ='bold')
ax.grid(True)

ax.set_title('matplotlib.axes.Axes.set_ylabel() Examples\n', fontsize = 14, fontweight ='bold')
plt.show()
