# Import packages necessary to create colorbar
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# make this example reproducible
np.random.seed(2)

#create chart
fig, ax = plt.subplots()
im = ax.imshow(np.random.rand(10,10))
ax.set_xlabel('x-axis label')

#add color bar
fig.colorbar(im)

plt.show()
