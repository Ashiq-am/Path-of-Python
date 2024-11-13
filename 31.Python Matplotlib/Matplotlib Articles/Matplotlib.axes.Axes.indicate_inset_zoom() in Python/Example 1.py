# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()


Z2 = np.zeros([150, 150], dtype ="g")

axins = ax.inset_axes([0.5, 0.5, 0.47, 0.47])
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

ax.indicate_inset_zoom(axins)

ax.set_title('matplotlib.axes.Axes.indicate_inset_zoom() Example',
			fontsize = 14, fontweight ='bold')
plt.show()
