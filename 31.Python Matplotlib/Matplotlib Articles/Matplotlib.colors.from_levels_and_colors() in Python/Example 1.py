import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

data1 = 3 * np.random.random((10, 10))
data2 = 5 * np.random.random((10, 10))

levels = [0, 1, 2, 3, 4, 5]
colors = ['red', 'brown',
          'yellow', 'green',
          'blue']
cmap, norm = matplotlib.colors.from_levels_and_colors(levels,
                                                      colors)

fig, axes = plt.subplots(ncols=2)

for ax, dat in zip(axes, [data1, data2]):
    im = ax.imshow(dat,
                   cmap=cmap,
                   norm=norm,
                   interpolation='none')

    fig.colorbar(im, ax=ax, orientation='horizontal')

plt.show()
