# Implementation of matplotlib function
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

delta = 0.25
x = np.arange(-3.0, 5.0, delta)
y = np.arange(-1.3, 2.5, delta)
X, Y = np.meshgrid(x, y)
Z = (np.exp(-X**2 - Y**2) - np.exp(-(X - 1)**2 - (Y - 1)**2))

fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation ='bilinear',
			origin ='lower',
			cmap ="bone",
			extent =(-3, 3, -2, 2))

levels = np.arange(-1.2, 1.6, 0.2)
CS = ax.contour(Z, levels,
				origin ='lower',
				cmap ='Greens',
				linewidths = 2,
				extent =(-3, 3, -2, 2))

zc = CS.collections[6]
plt.setp(zc, linewidth = 2)

ax.clabel(CS, levels,
		inline = 1,
		fmt ='% 1.1f',
		fontsize = 14)

plt.title('matplotlib.pyplot.contour() Example')
plt.show()
