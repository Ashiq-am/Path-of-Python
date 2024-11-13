import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Creating dataset
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)

fig = plt.figure(figsize =(24, 20))
gs = gridspec.GridSpec(nrows = 3, ncols = 2,
					height_ratios =[1, 1, 2])

# Varying the density along a
# streamline
ax = fig.add_subplot(gs[0, 0])
ax.streamplot(X, Y, U, V,
			density =[0.4, 0.8])

ax.set_title('Varying the density along a streamline')

# show plot
plt.tight_layout()
plt.show()
