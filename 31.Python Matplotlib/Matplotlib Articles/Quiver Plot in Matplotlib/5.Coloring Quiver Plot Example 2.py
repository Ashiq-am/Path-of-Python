# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Creating arrow
x = np.arange(0, 2 * np.pi + 2 * np.pi / 20,
			2 * np.pi / 20)
y = np.arange(0, 2 * np.pi + 2 * np.pi / 20,
			2 * np.pi / 20)

X, Y = np.meshgrid(x, y)

u = np.sin(X)*np.cos(Y)
v = -np.cos(X)*np.sin(Y)

# Defining color
color = np.sqrt(((dx-n)/2)*2 + ((dy-n)/2)*2)

# Creating plot
fig, ax = plt.subplots(figsize =(14, 9))
ax.quiver(X, Y, u, v, color, alpha = 1)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.axis([0, 2 * np.pi, 0, 2 * np.pi])
ax.set_aspect('equal')

# show plot
plt.show()
