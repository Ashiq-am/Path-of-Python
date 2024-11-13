import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection
import numpy as np


xy = np.random.random((10, 2))
z = np.random.random(10)

patches = [RegularPolygon((x, y),
						5, 0.1)
		for x, y in xy]

collection = PatchCollection(patches,
							array = z,
							edgecolors ='brown',
							lw = 2)

fig, ax = plt.subplots()

ax.patch.set(facecolor ='green')
ax.add_collection(collection)
ax.autoscale()

plt.show()
