import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable

res = np.array([[0, 2], [3, 4]], dtype = int)

u = np.unique(res)
bounds = np.concatenate(([res.min()-1],
						u[:-1]+np.diff(u)/2.,
						[res.max()+1]))

norm = colors.BoundaryNorm(bounds, len(bounds)-1)
color_map1 = ['#7fc97f', '#ffff99',
			'#386cb0', '#f0027f']
color_map = colors.ListedColormap(color_map1)

fig, axes = plt.subplots()
img = axes.imshow(res, cmap = color_map,
				norm = norm)
divider = make_axes_locatable(axes)
cax = divider.append_axes("right", size ="5 %")

color_bar = plt.colorbar(img, cmap = color_map,
						norm = norm, cax = cax)

color_bar.set_ticks(bounds[:-1]+np.diff(bounds)/2.)
color_bar.ax.set_yticklabels(color_map1)
color_bar.ax.tick_params(labelsize = 10)

plt.show()
