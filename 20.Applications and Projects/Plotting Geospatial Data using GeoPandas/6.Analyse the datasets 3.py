from mpl_toolkits.axes_grid1 import make_axes_locatable


fig, ax = plt.subplots(1, figsize =(16, 8),
					facecolor ='lightblue')

world.plot(ax = ax, color ='black')
world.plot(ax = ax, column ='pop_est', cmap ='Reds',
		edgecolors ='grey')

# axis for the color bar
div = make_axes_locatable(ax)
cax = div.append_axes("right", size ="3 %", pad = 0.05)

# color bar
vmax = world.pop_est.max()
mappable = plt.cm.ScalarMappable(cmap ='Reds',
								norm = plt.Normalize(vmin = 0, vmax = vmax))
cbar = fig.colorbar(mappable, cax)

ax.axis('off')
plt.show()
