import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

a = np.linspace(0, 3 * np.pi, 500)
b = np.sin(a)
# this is the first derivative
dbda = np.cos(0.5 * (a[:-1] + a[1:]))

# Createing line segments so
# to color them individually
points = np.array([a, b]).T.reshape(-1, 1, 2)
set_of_segments = np.concatenate([points[:-1],
								points[1:]],
								axis = 1)

figure, axes = plt.subplots(2, 1, sharex = True, sharey = True)

# Mapping the data points with
# continous norm
continous_norm = plt.Normalize(dbda.min(),
							dbda.max())

line_collection = LineCollection(set_of_segments,
								cmap ='viridis',
								norm = continous_norm)

# Set the values used for
# colormapping
line_collection.set_array(dbda)
line_collection.set_linewidth(2)
line = axes[0].add_collection(line_collection)
figure.colorbar(line, ax = axes[0])

# Use a boundary norm instead
cmap = ListedColormap(['r', 'g', 'b'])
boundary_norm = BoundaryNorm([-1, -0.5, 0.5, 1],
							cmap.N)

line_collection = LineCollection(set_of_segments,
								cmap = cmap,
								norm = boundary_norm)

line_collection.set_array(dbda)
line_collection.set_linewidth(2)
line = axes[1].add_collection(line_collection)
figure.colorbar(line, ax = axes[1])

axes[0].set_xlim(a.min(), a.max())
axes[0].set_ylim(-1.1, 1.1)
plt.show()
