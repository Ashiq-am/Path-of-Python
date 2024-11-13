# importing libraries
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# setup data
a = np.random.rand(10, 10)
im = plt.imshow(a, cmap="bwr")
cb = plt.colorbar(im, orientation='horizontal')

# change the label size
im.figure.axes[0].tick_params(axis="both", labelsize=21)

plt.show()
