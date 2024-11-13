# Implementation of matplotlib function
from cycler import cycler
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3 * np.pi)

offsets = np.linspace(0, 3 * np.pi, 8,
					endpoint = False)

yy = np.transpose([2 * np.sin(x + phi) for phi in offsets])

plt.rc('lines', linewidth = 4)
plt.rc('axes', prop_cycle =(cycler(color =['r', 'g',
										'purple',
										'orange']) +
						cycler(linestyle =['-',
											'--',
											':',
											'-.'])))

fig, (ax0, ax1) = plt.subplots(nrows = 2)
ax0.plot(yy)
ax0.set_title('Above example with set_prop_cycle() function\n\nSet default color cycle to rgby',
			fontsize = 12, fontweight ='bold')

ax1.set_prop_cycle(color =['magenta', 'g',
						'y', 'k'],
				lw =[1, 2, 3, 4])
ax1.plot(yy)
ax1.set_title('Set axes color cycle to cmyk',
			fontsize = 12,
			fontweight ='bold')

plt.show()
