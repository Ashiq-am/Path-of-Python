from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


# function for z axea
def f(x, y):
	return np.sin(np.sqrt(x ** 2 + y ** 2))

# x and y axis
x = np.linspace(-1, 5, 10)
y = np.linspace(-1, 5, 10)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot_wireframe(X, Y, Z, color ='green')
ax.set_title('wireframe geeks for geeks');
