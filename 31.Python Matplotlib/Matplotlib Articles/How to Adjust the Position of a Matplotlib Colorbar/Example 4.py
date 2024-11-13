import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# make this example reproducible
np.random.seed(1)

# create chart
fig, ax = plt.subplots()
im = ax.imshow(np.random.rand(15, 15))
ax.set_xlabel('x-axis label')
ax.set_title('Colorbar above chart')

# add color bar below chart
divider = make_axes_locatable(ax)
cax = divider.new_vertical(size = '5%', pad = 0.5)
fig.add_axes(cax)
fig.colorbar(im, cax = cax, orientation = 'horizontal')

plt.show()
