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

# Controlling the starting points
# of the streamlines
seek_points = np.array([[-2, -1, 0, 1, 2, -1],
						[-2, -1, 0, 1, 2, 2]])

ax = fig.add_subplot(gs[1, 1])
strm = ax.streamplot(X, Y, U, V, color = U,
					linewidth = 2,
					cmap ='autumn',
					start_points = seek_points.T)

fig.colorbar(strm.lines)
ax.set_title('Controlling the starting points of the streamlines')

# Displaying the starting points
# with blue symbols.
ax.plot(seek_points[0], seek_points[1], 'bo')
ax.set(xlim =(-w, w), ylim =(-w, w))

# show plot
plt.tight_layout()
plt.show()
