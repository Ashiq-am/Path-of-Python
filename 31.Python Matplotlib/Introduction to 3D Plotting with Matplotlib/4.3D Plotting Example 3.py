#importing matplotlib.pyplot from
# python
import matplotlib.pyplot as plt

# importing numpy package from python
import numpy as np

# creating an empty figure for plotting
fig = plt.figure()

# defining a sub-plot with 1x2 axis and defining
# it as first plot with projection as 3D
ax = fig.add_subplot(1, 2, 1, projection='3d')

# creating a range of 12 elements in both
# X and Y
X = np.arange(12)
Y = np.linspace(12, 1)

# Creating a mesh grid of X and Y
X, Y = np.meshgrid(X, Y)

# Creating an expression X and Y and
# storing it in Z
Z = X*2+Y*3;

# Creating a wireframe plot with the 3 sets of
# values X,Y and Z
ax.plot_wireframe(X, Y, Z)

# Creating my second subplot with 1x2 axis and defining
# it as the second plot with projection as 3D
ax = fig.add_subplot(1, 2, 2, projection='3d')

# defining a set of points for X,Y and Z
X1 = [1,2,1,4,3,2,7,5,9]
Y1 = [8,2,7,4,3,6,1,8,9]
Z1 = [1,2,4,7,9,6,7,6,9]

# Plotting 3 points X1,Y1,Z1 with
# color as green
ax.plot(X1, Y1, Z1,color='green')

# Showing the above plot
plt.show()
