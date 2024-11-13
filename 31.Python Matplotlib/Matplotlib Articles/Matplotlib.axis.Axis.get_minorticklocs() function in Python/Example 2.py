# Implementation of matplotlib function
from matplotlib.axis import Axis
from matplotlib.artist import Artist
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data(0.1)
ax.plot_wireframe(X, Y, Z, rstride=5,
                  cstride=5)

ax.view_init(30, 50)
fig.canvas.draw()
renderer = fig.canvas.renderer
Artist.draw(ax, renderer)
ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(8))

fig.suptitle('Matplotlib.axis.Axis.get_minorticklocs()\n\
Function Example')
ax.grid()

print("Value of get_minorticklocs() :")
for i in ax.xaxis.get_minorticklocs():
    print(i)

plt.show()
