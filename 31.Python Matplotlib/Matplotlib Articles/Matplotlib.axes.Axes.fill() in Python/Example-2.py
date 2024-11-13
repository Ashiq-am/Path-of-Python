# Implementation of matplotlib function

import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt

theta = np.deg2rad(np.arange(0.0, 360.0, 1.0))
x = 0.5 * np.cos(theta)
y = 0.5 * np.sin(theta)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(9, 3),
                                    subplot_kw={'aspect': 'equal'},
                                    sharey=True)
ax1.fill(x, y, facecolor='green')
ax1.set_title('Fig 1')

ax2.fill(x, y, facecolor='green', edgecolor='black',
         linewidth=4)

ax2.set_title('Fig 2')

ax3.fill(x, y, facecolor='none', edgecolor='green',
         linewidth=4)
ax3.set_title('Fig 3')

plt.show()
