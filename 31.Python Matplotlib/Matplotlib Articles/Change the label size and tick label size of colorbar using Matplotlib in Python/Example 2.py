# importing libraries
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# setup data
a = np.random.rand(10, 10)
im = plt.imshow(a, cmap="bwr")
cb = plt.colorbar(im, orientation='horizontal')

# change the tick label size of colorbar
im.figure.axes[1].tick_params(axis="x", labelsize=18)

plt.show()
