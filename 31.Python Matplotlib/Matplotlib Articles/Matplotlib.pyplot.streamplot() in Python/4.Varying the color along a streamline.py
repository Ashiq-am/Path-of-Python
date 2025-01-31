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

# Varying color along a streamline
ax = fig.add_subplot(gs[0, 1])
strm = ax.streamplot(X, Y, U, V, color = U,
					linewidth = 2, cmap ='autumn')
fig.colorbar(strm.lines)
ax.set_title('Varying the color along a streamline.')

# show plot
plt.tight_layout()
plt.show()
