import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

# dummy data to build the grid
data = np.random.rand(10, 10) * 20

# converting into hex color
# code with alpha set to True
hex_color = matplotlib.colors.to_hex([ 0.47,
									0.0,
									1.0,
									0.5 ],
									keep_alpha = True)

# create discrete colormap
cmap = colors.ListedColormap([hex_color,
							'red'])

bounds = [0, 10, 20]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(data, cmap = cmap, norm = norm)

# draw gridlines
ax.grid(which ='major', axis ='both',
		linestyle ='-', color ='k',
		linewidth = 2)

ax.set_xticks(np.arange(-.5, 10, 1))
ax.set_yticks(np.arange(-.5, 10, 1))

plt.show()
