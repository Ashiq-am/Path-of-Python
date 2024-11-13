# importing libraries
import numpy as np
from matplotlib import pyplot as plt

# setup data
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
data = np.random.rand(6, 6)
im = plt.imshow(data, interpolation="nearest", cmap="Accent")
cbar = plt.colorbar(im)

# change the label size
im.figure.axes[0].tick_params(axis="both", labelsize=21)

# change the tick label size of colorbar
im.figure.axes[1].tick_params(axis="y", labelsize=21)

plt.show()
