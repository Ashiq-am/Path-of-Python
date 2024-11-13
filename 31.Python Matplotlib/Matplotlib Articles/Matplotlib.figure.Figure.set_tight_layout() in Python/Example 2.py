# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np

# Create triangulation.
x = np.asarray([0, 1, 2, 3,
                0.5, 1.5,
                2.5, 1, 2,
                1.5])

y = np.asarray([0, 0, 0, 0,
                1.0, 1.0, 1.0,
                2, 2, 3.0])

triangles = [[0, 1, 4], [1, 5, 4],
             [2, 6, 5], [4, 5, 7],
             [5, 6, 8], [5, 8, 7],
             [7, 8, 9], [1, 2, 5],
             [2, 3, 6]]

triang = mtri.Triangulation(x, y, triangles)
z = np.cos(1.5 * x) * np.cos(1.5 * y)

fig, axs = plt.subplots()

axs.tricontourf(triang, z)
axs.triplot(triang, 'go-', color='white')
fig.tight_layout(rect=(0.1, 0.1, 0.95, 0.95))

fig.set_tight_layout(False)

fig.canvas.draw()

fig.suptitle("""matplotlib.figure.Figure.set_tight_layout() 
function Example\n\n""", fontweight="bold")

plt.show()
