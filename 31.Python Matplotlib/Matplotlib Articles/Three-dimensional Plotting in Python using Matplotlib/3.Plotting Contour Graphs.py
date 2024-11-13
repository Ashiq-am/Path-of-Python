from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


# function for z axis
def f(x, y):
	return np.sin(np.sqrt(x ** 2 + y ** 3))

# x and y axis
x = np.linspace(-1, 5, 10)
y = np.linspace(-1, 5, 10)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection ='3d')

# ax.contour3D is used plot a contour graph
ax.contour3D(X, Y, Z)
