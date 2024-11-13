import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors


# ADJUSTABLE VARIABLES, defining the setup (Units : SI)
D = 5		 # distance of screen
slitWidth = 0.0001
slitHeight = 0.005
# amplitude/intensity
a = 1
# wavelength
w = 0.0000006
x1 = -0.25
# assuming screen is a rectangle from (x1,y1) to (x2,y2)
x2 = 0.25
y1 = -0.025
y2 = 0.025
# linear resolution (no. of points per unit length)
lres = 5000


# PERFORMING CALCULATIONS
# calculations are performed using numpy arrays and array methods
m, n = int((x2-x1)*lres), int((y2-y1)*lres)

# Obtaining sample points on the screen -
# X, Y and Z are mxn 2d arrays containing x coordinates, y coordinates
# and z coordinates of the screen sample-points respectively.
X = np.linspace(x1, x2, n)
Y = np.linspace(y1, y2, m)
X, Y = np.meshgrid(X, Y)
Z = np.ones((m, n))*D


# Dividing the slit into sample points
# xcoords contains the x coordinates of the sample points
# ycoords contains the y coordinates of the sample points
xcoords = np.linspace(-slitWidth/2, slitWidth/2, 20)
ycoords = np.linspace(-slitHeight/2, slitHeight/2, 100)

# calculating the amplitude/intensity at each point (using superposition)
# first the intensity is initialised as zero
# then the intensity due to each sample point on the slit is added in the loop
A = np.zeros((m, n))
for i in ycoords:
	for j in xcoords:
		L = np.sqrt(np.square(X-np.ones((m, n))*j) +
					np.square(Y-np.ones((m, n))*i) + np.square(Z))
		theta = (L/w) * 2 * np.pi
		A += a * np.sin(theta)

A = np.abs(A)


# PLOTTING
# following steps set the axes, labels and title
ax = plt.axes()
ax.set_aspect('equal')
plt.rc('text', usetex=False) # this tells matplotlib that tex has been used in titles and labels
plt.title("Single Slit Diffraction Pattern Simulation\nD = {}m, slit-width = {}m, slit-height = {}m, $\lambda$ = {}m".format(D, slitWidth, slitHeight, w))
plt.xlabel("x-axis of screen (metres)")
plt.ylabel("y-axis (metres)")

# follwing step plots the heatmap of 2D-array A
graph = plt.pcolormesh(
	X, Y, A, cmap=matplotlib.colors.LinearSegmentedColormap.from_list("", ['black', 'red']))

# following step adds the scale of the heatmap to the figure
plt.colorbar(graph, orientation='horizontal')
plt.show()
