# Implementation of matplotlib function
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data(0.1)
ax.plot_wireframe(X, Y, Z, rstride=5,
                  cstride=5)

for angle in range(0, 90):
    ax.view_init(30, angle)
    fig.canvas.draw()
    renderer = fig.canvas.renderer
    fig.draw(renderer)
    plt.pause(.001)

    fig.suptitle('matplotlib.figure.Figure.draw() \
    function Example')
