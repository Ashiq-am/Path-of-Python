# importing axes3d from mpl_toolkits.mplot
# module in python
from mpl_toolkits.mplot3d import axes3d

# importing matplotlib package from python
import matplotlib.pyplot as plt

#importing numpy package from
# python library
import numpy as np

# Creating an empty figure
fig = plt.figure()

# Creating a subplot where we are
# defining the projection as 3D projection
ax = fig.add_subplot(1,2,1, projection='3d')

# Creating a set of testing data using
# get_test_data from axes3d module in
# python. It creates a set of nD arrays
# for each of the variables X,Y,Z
X, Y, Z = axes3d.get_test_data(0.07)
#Plotting the contour plot with the
# following range of nD arrays
plot = ax.contour(X, Y, Z)

# Adding a second subplot in our figure with
# the projection as a 3D projection
ax=fig.add_subplot(1,2,2,projection='3d')

# Adding a range of values to the variables X1,Y1
X1=[1,2,3,4,5,6,7]
Y1=[1,2,3,4,5,6,7]

# Creating a meshgrid of X1 and Y1
X1, Y1 = np.meshgrid(X1,Y1)
# Creating an expression for Z1 with the
# help of X1 and Y1
Z1=(X1+4)*5+(Y1-5)/2

# Creating a contour plot
plot2 = ax.contourf(X1, Y1, Z1)

# Showing the above plot
plt.show()
