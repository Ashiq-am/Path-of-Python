# importing numpy package
import numpy as np

# importing matplotlib package
import matplotlib.pyplot as plt

# importing mplot3d from
# mpl_toolkits
from mpl_toolkits import mplot3d

# creating an empty canvas
fig = plt.figure()

# defining the axes with the projection
# as 3D so as to plot 3D graphs
ax = plt.axes(projection="3d")

# creating a wide range of points x,y,z
x=[0,1,2,3,4,5,6]
y=[0,1,4,9,16,25,36]
z=[0,1,4,9,16,25,36]

# plotting a 3D line graph with X-coordinate,
# Y-coordinate and Z-coordinate respectvely
ax.plot3D(x, y, z, 'red')

# plotting a scatter plot with X-coordinate,
# Y-coordinate and Z-coordinate respectvely
# and defining the points color as cividis
# and defining c as z which basically is a
# defination of 2D array in which rows are RGB
#or RGBA
ax.scatter3D(x, y, z, c=z, cmap='cividis');

# Showing the above plot
plt.show()
