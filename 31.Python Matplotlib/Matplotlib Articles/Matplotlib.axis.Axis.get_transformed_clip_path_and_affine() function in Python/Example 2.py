# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

delta = 0.025

x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)

Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
Z = (Z1 - Z2) * 2

path = Path([[0, 1], [1, 0], [0, -1], [-1, 0], [0, 1]])
patch = PathPatch(path, facecolor='none')

fig, ax = plt.subplots()
ax.add_patch(patch)
im = ax.imshow(Z,
               interpolation='bilinear',
               cmap=cm.gray,
               origin='lower',
               extent=[-3, 3, -3, 3],
               clip_path=patch,
               clip_on=True)

# use of get_transformed_clip_path_and_affine() method
val = Axis.get_transformed_clip_path_and_affine(im)
print("Value Return by get_transformed_clip_path_and_affine(): ")
for i in val:
    print(i)

fig.suptitle("""matplotlib.axis.Axis.get_transformed_clip_path_and_affine() 
function Example\n""", fontweight="bold")

plt.show()
