import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt


# setup the plot
figure, axes = plt.subplots(1, 1,
							figsize=(6, 6))

# defining random data
x = np.random.rand(20)
y = np.random.rand(20)
tag = np.random.randint(0, 20, 20)
tag[10:12] = 0

# defining the colormap
cmap = plt.cm.jet

# extracting all colors
cmaplist = [cmap(i) for i in range(cmap.N)]

# making first color entry grey
cmaplist[0] = (.5, .5, .5, 1.0)

# new map
cmap = mpl.colors.LinearSegmentedColormap.from_list(
'Custom cmap', cmaplist, cmap.N)

# defining the bins and norms
bounds = np.linspace(0, 20, 21)
norm = mpl.colors.BoundaryNorm(bounds,
							cmap.N)

# the scatter
scat = axes.scatter(x, y, c=tag,
					s=np.random.randint(100,
										500,
										20),
					cmap=cmap, norm=norm)

# axes for the colorbar
ax2 = figure.add_axes([0.95, 0.1,
					0.03, 0.8])


axes.set_title(' discrete colors')
