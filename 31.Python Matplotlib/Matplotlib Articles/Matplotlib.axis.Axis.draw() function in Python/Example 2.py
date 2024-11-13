# Implementation of matplotlib function
from matplotlib.axis import Axis
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data(0.1)
ax.plot_wireframe(X, Y, Z, rstride=5,
                  cstride=5)

ax.view_init(30, 60)
fig.canvas.draw()
renderer = fig.canvas.renderer
ax.draw(renderer)

ax.grid()

fig.suptitle("""matplotlib.axis.Axis.draw() 
function Example\n""", fontweight="bold")

plt.show()
