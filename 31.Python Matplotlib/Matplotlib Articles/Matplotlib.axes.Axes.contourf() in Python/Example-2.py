# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

# invent some numbers, turning the
# x and y arrays into simple 2d arrays,
# which make combining them together easier.
x = np.linspace(-3, 15, 450).reshape(1, -1)
y = np.linspace(-3, 15, 720).reshape(-1, 1)
z = np.cos(x)*2 - np.sin(y)**2

# we no longer need x and y to be
# 2 dimensional, so flatten them.
x, y = x.flatten(), y.flatten()

fig1, ax1 = plt.subplots()
cs = ax1.contourf(x, y, z, hatches =['-', '/', '\\', '//'],
				cmap ='Greens', extend ='both', alpha = 1)
fig1.colorbar(cs)
ax1.set_title('matplotlib.axes.Axes.contourf() Example')
plt.show()
