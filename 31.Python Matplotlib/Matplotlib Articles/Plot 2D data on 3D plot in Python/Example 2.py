# importing numpy package
import numpy as np
# importing matplotlib package
import matplotlib.pyplot as plt

# creating an empty canvas
fig = plt.figure()

# Creating an empty 3D axes of the plot
ax = fig.add_subplot(projection='3d')

# Labeling the X Axis
ax.set_xlabel('X Axis')

# Labeling the Y-Axis
ax.set_ylabel('Y Axis')

# Labeling the Z-Axis
ax.set_zlabel('Z Axis')

# Creating X as an array of numbers
# from 1 to 10
x = np.arange(11)

# Creating Y as an array of numbers
# which are sqaure of the numbers
# in X
y = x**2

# Creating a 2D data Scatter plot for the
# on a 3D axis figure
ax.scatter(x, y, c='b')

# Showing the above 3D plot
plt.show()
