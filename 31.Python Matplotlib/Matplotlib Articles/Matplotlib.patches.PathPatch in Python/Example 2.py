import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch


fig = plt.figure()

ax = fig.add_subplot(111, aspect ='equal')
path = Path([[0, 0], [0, 1], [1, 0], [0, 0]])
patch = PathPatch(path, facecolor ='none')
ax.add_patch(patch)

Z, Z2 = np.meshgrid(np.linspace(0, 1), np.linspace(0, 1))

im = plt.imshow(Z-Z2,
				interpolation ='bilinear',
				cmap = plt.cm.RdYlGn,
				origin ='lower',
				extent =[0, 1, 0, 1],
				clip_path = patch,
				clip_on = True)

im.set_clip_path(patch)

ax.set_xlim((0, 1))
ax.set_ylim((0, 1))

plt.show()
