import numpy as np
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import animation

fig, ax = plt.subplots()

patches = []
# create circles with random sizes
# and locations
N = 12  # number of circles
x = np.random.rand(N)
y = np.random.rand(N)
radii = 0.1 * np.random.rand(N)
for x1, y1, r in zip(x, y, radii):
    circle = Circle((x1, y1), r)
    patches.append(circle)

# add these circles to a collection
p = PatchCollection(patches, cmap=cm.prism, alpha=0.4)
ax.add_collection(p)


def animate(i):
    # random index to color map
    colors = 100 * np.random.rand(len(patches))

    # set new color colors
    p.set_array(np.array(colors))
    return p,


ani = animation.FuncAnimation(fig, animate,
                              frames=50, interval=50)

plt.show()
