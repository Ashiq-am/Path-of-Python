# importing matplotlib.pyplot from
# python
import matplotlib.pyplot as plt

# importing numpy package from
# python
import numpy as np

# creating a range of values for
# x,y,x1,y1 from -5 to 5 with
# a space of 1 between the elements
x = np.arange(-5,5,1)
y = np.arange(-5,5,1)

# creating a range of values for
# x,y,x1,y1 from -5 to 5 with
# a space of 0.6 between the elements
x1= np.arange(-5,5,0.6)
y1= np.arange(-5,5,0.6)

# Creating a mesh grid with x ,y and x1,
# y1 which creates an n-dimentional
# array
x, y = np.meshgrid(x, y)
x1,y1= np.meshgrid(x1,y1)

# Creating a sine function with the
# range of values from the meshgrid
z = np.sin(x * np.pi/2 )

# Creating a cosine function with the
# range of values from the meshgrid
z1= np.cos(x1* np.pi/2)

# Creating an empty figure for
# 3D plotting
fig = plt.figure()

# using fig.gca, we are creating a 3D
# projection plot in the empty figure
ax = fig.gca(projection="3d")

# Creating a wireframe plot with the x,y and
# z-coordinates respectively along with the
# color as red
surf = ax.plot_wireframe(x, y, z, color="red")

# Creating a wireframe plot with the points
# x1,y1,z1 along with the plot line as green
surf1 =ax.plot_wireframe(x1, y1, z1, color="green")

#showing the above plot
plt.show()
