import numpy as np
import matplotlib
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import matplotlib.patches as matpatches


fig, ax = plt.subplots(figsize =(8, 8))
patches = []


circle = Circle((2, 2), 2)
patches.append(circle)



polygon = matpatches.PathPatch(patches[0].get_path())
patches.append(polygon)


colors = 2 * np.random.rand(len(patches))
p = PatchCollection(patches,
					cmap = matplotlib.cm.jet,
					alpha = 0.4)

p.set_array(np.array(colors))
ax.add_collection(p)

plt.axis([-10, 10, -10, 10])

plt.show()
