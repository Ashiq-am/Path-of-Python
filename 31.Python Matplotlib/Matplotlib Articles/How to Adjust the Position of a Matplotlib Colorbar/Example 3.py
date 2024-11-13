import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# make this reproducible
np.random.seed(2)

# create chart
fig, ax = plt.subplots()
im = ax.imshow(np.random.rand(10,10))
ax.set_xlabel('x-axis label')

# add color bar below chart
divider = make_axes_locatable(ax)
cax = divider.new_vertical(size='5%', pad=0.6, pack_start = True)
fig.add_axes(cax)
fig.colorbar(im, cax = cax, orientation = 'horizontal')

plt.show()
