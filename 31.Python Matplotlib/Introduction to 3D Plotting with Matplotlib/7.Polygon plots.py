# import Axes3D from mpl_toolkits.mplot3d
# from python
from mpl_toolkits.mplot3d import Axes3D

# importing PolyCollection from
# matplotlib.collections module
from matplotlib.collections import PolyCollection

#importing matplotlib.pyplot from
# python
import matplotlib.pyplot as plt

# importing numpy package from
# python
import numpy as np

# Creating an empty figure
fig = plt.figure()

# Creating a 3D projection using
# fig.gca
ax = fig.gca(projection='3d')

# Creating a wide range of elements
# using numpy package from python
xs = np.arange(0, 1, 0.1)
# Creating an empty list
verts = []
# Creating a range of values on
# Z-Axis
zs = [0.0, 0.2, 0.4, 0.6,0.8]
# Looping through all the values in zs
# and creating random values in ys using
# np.random.rand() which creates a range of
# elements in ys and we are appending each of them
# inside verts[]
for z in zs:
	ys = np.random.rand(len(xs))
	verts.append(list(zip(xs, ys)))
# using polycollection, we are providing a
# series of vertices to poly so as to
# plot our required plot
poly = PolyCollection(verts)
# Using add_collection3d, we are plotting
# ur required ploygon plot where we define
# zs with the range of values we defined in our
# list zs and also the zdir as Y-Axis
ax.add_collection3d(poly,zs=zs,zdir='y')
# Showing the required plot
plt.show()
