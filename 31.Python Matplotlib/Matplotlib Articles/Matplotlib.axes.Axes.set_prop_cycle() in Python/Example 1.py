# Implementation of matplotlib function
from cycler import cycler
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 200, 10)

yy = np.transpose([2 * np.sin(x + phi) for phi in x])

fig, ax1 = plt.subplots()

ax1.set_prop_cycle(color =['magenta', 'g',
						'y', 'k'],
				lw =[1, 2, 3, 4])
ax1.plot(yy)
ax1.set_title(' matplotlib.axes.Axes.set_prop_cycle() Example\n', fontsize = 12, fontweight ='bold')
plt.show()
