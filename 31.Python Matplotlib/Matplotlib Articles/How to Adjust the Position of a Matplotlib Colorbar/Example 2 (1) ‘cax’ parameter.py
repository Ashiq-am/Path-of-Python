import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# make this example reproducible
np.random.seed(1)

# create chart
fig = plt.figure()
ax = fig.add_subplot(111)
axp = ax.imshow(np.random.randint(0, 10, (10, 10)))
ax.set_title('Colorbar on left')

# Adding the colorbar
cbaxes = fig.add_axes([0.1, 0.1, 0.03, 0.8])

# position for the colorbar
cb = plt.colorbar(axp, cax = cbaxes)
plt.show()
