# Import libraries
import numpy as np
import matplotlib.pyplot as plt


# Creating arrows
x = np.arange(-2, 2.2, 0.2)
y = np.arange(-2, 2.2, 0.2)

# Creating gradient
X, Y = np.meshgrid(x, y)
z = X * np.exp(-X**2-Y**2)
dx, dy = np.gradient(z)

# Creating plot
fig, ax = plt.subplots(figsize =(9, 9))
ax.quiver(X, Y, dx, dy)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_aspect('equal')

# show plot
plt.show()
