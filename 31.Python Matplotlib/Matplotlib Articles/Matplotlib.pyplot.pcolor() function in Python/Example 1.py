# Demonstration of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

Z = np.random.rand(4, 12)

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(Z)
ax0.set_title('No edge image')

c = ax1.pcolor(Z, edgecolors='k', linewidths=5)
ax1.set_title('Thick edges image')

fig.tight_layout()
plt.show()
