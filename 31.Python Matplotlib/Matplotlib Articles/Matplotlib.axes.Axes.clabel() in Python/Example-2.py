# Implementation of matplotlib function
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z = (np.exp(-X**2 - Y**2) - np.exp(-(X - 1)**2 - (Y - 1)**2)) * 3

fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation ='bilinear', origin ='lower',
			cmap ="Greens", extent =(-3, 3, -2, 2))

levels = np.arange(-1.2, 1.6, 0.2)
CS = ax.contour(Z, levels, origin ='lower', cmap ='spring',
				linewidths = 2, extent =(-3, 3, -2, 2))
zc = CS.collections[6]
plt.setp(zc, linewidth = 4)

ax.clabel(CS, levels[1::2], inline = 1, fmt ='% 1.1f',
		fontsize = 14)

CB = fig.colorbar(CS, shrink = 0.8, extend ='both')
CBI = fig.colorbar(im, orientation ='horizontal',
				shrink = 0.8)

ax.set_title('matplotlib.axes.Axes.clabel() Example')
plt.show()
