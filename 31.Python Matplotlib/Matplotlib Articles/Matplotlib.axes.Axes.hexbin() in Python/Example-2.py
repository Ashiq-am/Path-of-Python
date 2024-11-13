# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

n = 100000
x = np.random.standard_normal(n)
y = 2 * np.random.standard_normal(n)
z =[1, 2, 3, 4]
xmin = x.min()
xmax = x.max()
ymin = y.min()
ymax = y.max()

fig, axs = plt.subplots(ncols = 3,
						sharey = True)

ax = axs[0]
hb = ax.hexbin(x, y, gridsize = 50,
			bins ='log',
			cmap ='BuGn')

ax.set(xlim =(xmin, xmax),
	ylim =(ymin, ymax))

cb = fig.colorbar(hb, ax = ax)
cb.set_label('log')

ax = axs[1]
hb = ax.hexbin(x, y, gridsize = 50,
			cmap ='Greens')

ax.set(xlim =(xmin, xmax),
	ylim =(ymin, ymax))

cb = fig.colorbar(hb, ax = ax)
cb.set_label('Values')

ax.set_title('matplotlib.axes.Axes.hexbin() Example')

ax = axs[2]
hb = ax.hexbin(x, y, gridsize = 50,
			bins = z, cmap ='BuGn')

ax.set(xlim =(xmin, xmax),
	ylim =(ymin, ymax))

cb = fig.colorbar(hb, ax = ax)
cb.set_label(z)
plt.show()
