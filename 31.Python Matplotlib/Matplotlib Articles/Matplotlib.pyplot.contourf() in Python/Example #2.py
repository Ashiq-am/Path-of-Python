# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

# invent some numbers, turning
# the x and y arrays into simple
# 2d arrays, which make combining
# them together easier.
x = np.linspace(-3, 15, 50).reshape(1, -1)
y = np.linspace(-3, 15, 20).reshape(-1, 1)
z = np.cos(x)*2 - np.sin(y)*2

# we no longer need x and y to
# be 2 dimensional, so flatten them.
x, y = x.flatten(), y.flatten()

cs = plt.contourf(x, y, z,
				hatches =['-', '/',
							'\\', '//'],
				cmap ='Greens',
				extend ='both',
				alpha = 1)

plt.colorbar(cs)

plt.title('matplotlib.pyplot.contourf() Example')
plt.show()
