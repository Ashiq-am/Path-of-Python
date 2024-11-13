# import axes3d from mpl_toolkits.mplot3d
from mpl_toolkits.mplot3d import axes3d

# import matplotlib.pyplot from python
import matplotlib.pyplot as plt

# import numoy from python
import numpy as np

# Creating an empty figure
# to plot a 3D graph
fig = plt.figure()

# Creating a 3Dprojection for
# our 3D plots using fig.gca
ax = fig.gca(projection='3d')

# Creating a meshgrid for the range
# of values in X,Y,Z
x, y, z = np.meshgrid([1,2,5,2,4,8,3,3,1],[6,4,3,1,6,2,7,8,2],[1,2,5,2,4,8,3,3,1])

# Creating expressions for u,v,w
# with the help of x,y and z
# which will form the direction vectors
u = x*2+y*3+z*3
v = (x+3)*(y+5)*(z+7)
w = x+y+z

# Creating a quiver plot with length of the direction
# vector length as 0.2 ad normalise as true
ax.quiver(x, y, z, u, v, w, length=0.2, normalize=True)

#showing the above plot
plt.show()
