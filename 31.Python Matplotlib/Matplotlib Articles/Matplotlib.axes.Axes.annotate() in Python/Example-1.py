# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots()

t = np.arange(4, 50., 1)
s = np.cos(np.pi * t)**3- np.sin(3 * np.pi * t)**2

ax1.plot(t, s, lw = 2)
ax1.annotate('Starting', xy =(3.3, 1),
			xytext =(3, 1.8),
			arrowprops = dict(facecolor ='green',
							shrink = 0.05), )

ax1.set_ylim(-2, 2)
ax1.set_title('matplotlib.axes.Axes.annotate() Example')
plt.show()
