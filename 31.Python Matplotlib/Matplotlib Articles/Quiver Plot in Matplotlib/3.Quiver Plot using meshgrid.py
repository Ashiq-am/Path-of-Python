# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Creating arrow
x = np.arange(0, 2.2, 0.2)
y = np.arange(0, 2.2, 0.2)

X, Y = np.meshgrid(x, y)
u = np.cos(X)*Y
v = np.sin(Y)*Y

# creating plot
fig, ax = plt.subplots(figsize =(14, 8))
ax.quiver(X, Y, u, v)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.axis([-0.3, 2.3, -0.3, 2.3])
ax.set_aspect('equal')

# show plot
plt.show()
